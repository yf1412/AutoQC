from dataio import wod
import json, glob, time
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import numpy as np
import os
import sys
import util.combineTests as combinatorics
import util.benchmarks as benchmarks

def readInput(JSONlist):
    '''Create a list of data file names from a json array.'''
    datafiles = json.loads(open(JSONlist).read())

    # assert that a list of data files is found, and all those files exist:
    assert type(datafiles) is list, 'Failed to read a list from datafiles.json'
    for i in datafiles:
      assert os.path.isfile(i), 'datafile ' + i + ' is not found.'

    return datafiles

def extractProfiles(filenames):
  '''Read all profiles from the files and store in a list. Only the profile
     descriptions are read, not the profile data, in order to avoid using
     too much memory.
  '''
  profiles = []
  for filename in filenames:
      with open(filename) as f:
          profiles.append(wod.WodProfile(f, load_profile_data=False))
          while profiles[-1].is_last_profile_in_file(f) == False:
              profiles.append(wod.WodProfile(f, load_profile_data=False))

  # assert all elements of profiles are WodProfiles
  for i in profiles:
    assert isinstance(i, wod.WodProfile), i + ' is not a WodProfile'

  return profiles

def catchFlags(profile):
  '''
  In some IQuOD datasets temperature values of 99.9 are special values to
  signify not to use the data value. These are flagged here so they are not
  sent to the quality control programs for testing.
  '''
  index = profile.var_index()
  assert index is not None, 'No temperatures in profile %s' % profile.uid()
  for i in range(profile.n_levels()):
      if profile.profile_data[i]['variables'][index]['Missing']:
          continue
      if profile.profile_data[i]['variables'][index]['Value'] == 99.9:
          profile.profile_data[i]['variables'][index]['Missing'] = True

def importQC(dir):
  '''
  return a list of names of tests found in <dir>:
  '''
  testFiles = glob.glob(dir+'/[!_]*.py')
  testNames = [testFile[len(dir)+1:-3] for testFile in testFiles]

  return testNames

def run(test, profiles, kwargs):
  '''
  run <test> on a list of <profiles>, return an array summarizing when exceptions were raised
  '''
  qcResults = []
  verbose = []
  for profile in profiles:
    exec('result = ' + test + '.test(profile, **kwargs)')

    #demand tests returned bools:
    for i in result:
      assert isinstance(i, np.bool_), str(i) + ' in test result list is of type ' + str(type(i))

    qcResults.append(np.any(result))
    verbose.append(result)
  return [qcResults, verbose]

def referenceResults(profiles):
  '''
  extract the summary reference result for each profile:
  '''
  refResult = []
  verbose = []
  for profile in profiles:
    refAssessment = profile.t_level_qc(originator=True) >= 3

    #demand reference results returned bools, or masked constants for missing values:
    for i in refAssessment:
      assert isinstance(i, np.bool_) or isinstance(i, np.ma.core.MaskedConstant), str(i) + ' in reference result list is of type ' + str(type(i))

    refResult.append(np.ma.any(refAssessment))
    verbose.append(refAssessment)
  return [refResult, verbose]

def generateLogfile(verbose, trueVerbose, profiles, testNames):
  '''
  verbose[i][j][k] == result of test i on profile j at depth k
  trueVerbose[j][k] == true result for profile j at depth k
  <profiles> == array of profiles per `extractProfiles`
  <testNames> == array of names returned by `importQC`
  '''
  # open a logfile
  logfile = open('AutoQClog.' + time.strftime("%H%M%S"), 'w')

  # log summary for each profile
  for i in range (0, len(profiles)): # i counts profiles
    with open(profiles[i].file_name) as f:
      f.seek(profiles[i].file_position)
      profile = wod.WodProfile(f)
      
    logfile.write('Profile ID: %i\n' % profiles[i].uid())

    # title row
    titleRow = 'Depth (m)  Temp (degC)'
    formatString = '{0[0]:<20}{0[1]:<20}'
    k = 2
    for test in testNames:
        titleRow += '  ' + test
        formatString += '{0['+str(k)+']:<20}'
        k += 1
    titleRow += '  Reference'
    formatString += '{0['+str(k)+']:<20}'
    logfile.write(formatString.format(titleRow.split('  ')))
    logfile.write('\n')

    # row for each depth
    for j in range (0,len(trueVerbose[i])): # j counts depth
      formatString = '{0[0]:<20}{0[1]:<20}'
      row = str(profile.z()[j]) + '  ' + str(profile.t()[j]) + '  '
      for k in range (0, len(verbose)): # k counts tests
        row += str(verbose[k][i][j])
        row += '  '
        formatString += '{0['+str(2+k)+']:<20}'
      row += str(trueVerbose[i][j])
      formatString += '{0['+str(2+len(verbose))+']:<20}'
      logfile.write(formatString.format(row.split('  ')))
      logfile.write('\n')

    summaryRow = '  OVERALL RESULTS:  '
    formatString = '{0[0]:<20}{0[1]:<20}'
    for k in range (0, len(verbose)):
      summaryRow += str(np.any(verbose[k][i]))
      summaryRow += '  '
      formatString += '{0['+str(2+k)+']:<20}'
    summaryRow += str(np.any(trueVerbose[i]))
    formatString += '{0['+str(2+len(verbose))+']:<20}'
    logfile.write(formatString.format(summaryRow.split('  ')))
    logfile.write('\n')

    logfile.write('-----------------------------------------\n')

def readENBackgroundCheckAux(testNames, kwargs):
  '''
  Reads auxiliary information needed by the EN background check.
  '''
  filename = 'data/EN_bgcheck_info.nc'
  if 'EN_background_check' in testNames and os.path.isfile(filename):
    nc = Dataset(filename)
    data = {}
    data['lon']   = nc.variables['longitude'][:]
    data['lat']   = nc.variables['latitude'][:]
    data['depth'] = nc.variables['depth'][:]
    data['month'] = nc.variables['month'][:]
    data['clim']  = nc.variables['potm_climatology'][:]
    data['bgev']  = nc.variables['bg_err_var'][:]
    data['obev']  = nc.variables['ob_err_var'][:]
    kwargs['EN_background_check_aux'] = data
  else:
    kwargs['EN_background_check_aux'] = None

########################################
# main
########################################

# identify data files and extract profile information into an array - this
# information is used by some quality control checks; the profile data are
# read later.
filenames = readInput('datafiles.json')
profiles = extractProfiles(filenames)
print('{} profiles will be read'.format(len(profiles)))

# identify and import tests
testNames = importQC('qctests')
testNames.sort()
print('{} quality control checks will be applied:'.format(len(testNames)))
for testName in testNames:
  print(' {}'.format(testName))
  exec('from qctests import ' + testName)

# Set up any keyword arguments needed by tests.
kwargs = {'profiles' : profiles}
readENBackgroundCheckAux(testNames, kwargs)

# run each test on each profile, and record its summary & verbose performance
testResults  = []
testVerbose  = []
trueResults  = []
trueVerbose  = []
firstProfile = True
delete       = []
currentFile  = ''
for iprofile, pinfo in enumerate(profiles):
  # Load the profile data.
  if pinfo.file_name != currentFile:
    if currentFile != '': f.close()
    currentFile = pinfo.file_name
    f = open(currentFile)
  if f.tell() != pinfo.file_position: f.seek(pinfo.file_position)
  p = wod.WodProfile(f)
  # Check that there are temperature data in the profile, otherwise skip.
  # A record is kept of the empty profiles.
  if p.var_index() is None:
    delete.append(iprofile)
    continue
  catchFlags(p)
  if np.sum(p.t().mask == False) == 0:
    delete.append(iprofile)
    continue
  # Run each test.    
  for itest, test in enumerate(testNames):
    result = run(test, [p], kwargs)
    if firstProfile:
      testResults.append(result[0])
      testVerbose.append(result[1])
    else:
      testResults[itest].append(result[0][0])
      testVerbose[itest].append(result[1][0])
  firstProfile = False
  # Read the reference result.
  truth = referenceResults([p])
  trueResults.append(truth[0][0])
  trueVerbose.append(truth[1][0])
  # Update user on progress.
  sys.stdout.write('{:5.1f}% complete\r'.format((iprofile+1)*100.0/len(profiles)))
  sys.stdout.flush()
# testResults[i][j] now contains a flag indicating the exception raised by test i on profile j

# Remove records of profiles with no temperature data.
for i in reversed(delete):
  del profiles[i]

# Summary statistics
print('Number of profiles tested was %i' % len(profiles))
for i in range (0, len(testNames)):
  print('Number of profiles that failed ' + testNames[i] + ' was %i' % np.sum(testResults[i]))
print('Number of profiles that should have been failed was %i' % np.sum(trueResults))

# generate a set of logical combinations of tests
combos = combinatorics.combineTests(testResults)
print('Number of combinations that were tried was %i' % len(combos))

# Compare the combinations to the truth.
bmResults = benchmarks.compare_to_truth(combos, trueResults)

# Plot the results.
benchmarks.plot_roc(bmResults)

#logfile
#generateLogfile(testVerbose, trueVerbose, profiles, testNames)

from cotede_qc.cotede_test import get_qc

def test(p):
    '''Run the density inversion QC from the CoTeDe Argo config.'''

    config   = {'TEMP': {'density_inversion': {
        'threshold': -0.03,
        'flag_good': 1,
        'flag_bad': 4} } }
    testname = 'density_inversion'

    return get_qc(p, config, testname)



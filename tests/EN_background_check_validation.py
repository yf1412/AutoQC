import qctests.EN_background_check
import util.testingProfile
import numpy

##### EN_background_check ---------------------------------------------------

def test_EN_background_check_findGridCell():
    '''
    check behavior of grid cell identifier:
    wrap around to the beginning of the list after exceeding the end by more than one cell;
    same idea at the beginning.
    '''

    gridLat  = [10,20,30,40]
    gridLong = [10,20,30,40]
    p = util.testingProfile.fakeProfile([0], [0], latitude=9, longitude=51) 

    ilon, ilat = qctests.EN_background_check.findGridCell(p, gridLong, gridLat)
    assert ilon == 0
    assert ilat == 3

def test_EN_background_check_findGridCell_even_spacing():
    '''
    findGridCell will silently fail if grid spacings are not even;
    check that asserts are raised checking for this.
    '''

    gridLat  = [10,21,28,40]
    gridLong = [10,20,30,40]
    p = util.testingProfile.fakeProfile([0], [0], latitude=29, longitude=51) 

    try:
        ilon, ilat = qctests.EN_background_check.findGridCell(p, gridLong, gridLat)
    except AssertionError:
        assert True
        return

    try:
        ilon, ilat = qctests.EN_background_check.findGridCell(p, gridLat, gridLong)
    except AssertionError:
        assert True
        return

    assert False, "findGridCell failed to raise an exception for unevenly spaced grid points"

def test_EN_background_check_estimatePGE():
    '''
    check the basic behavior of the probable gross error prior estimator
    '''

    assert qctests.EN_background_check.estimatePGE(1, False) == 0.05, 'incorrect non-suspect bathythermograph pge'
    assert qctests.EN_background_check.estimatePGE(16, True) == 0.525, 'incorrect suspect bathythermograph pge'
    assert qctests.EN_background_check.estimatePGE(4, False) == 0.01, 'incorrect non-suspect non-bathythermograph pge'




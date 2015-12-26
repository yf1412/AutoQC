from cotede_qc.cotede_test import get_qc

def test(p):
    '''Run the profile_envelop QC from the CoTeDe config.'''

    config   = {"TEMP": {
        "profile_envelop": [
            ["> 0", "<= 25", -2, 37],
            ["> 25", "<= 50", -2, 36],
            ["> 50", "<= 100", -2, 36],
            ["> 100", "<= 150", -2, 34],
            ["> 150", "<= 200", -2, 33],
            ["> 200", "<= 300", -2, 29],
            ["> 300", "<= 400", -2, 27],
            ["> 400", "<= 1100", -2, 27],
            ["> 1100", "<= 3000", -1.5, 18],
            ["> 3000", "<= 5500", -1.5, 7],
            ["> 5500", "<= 12000", -1.5, 4]
            ]
        }}
    testname = 'profile_envelop'

    return get_qc(p, config, testname)



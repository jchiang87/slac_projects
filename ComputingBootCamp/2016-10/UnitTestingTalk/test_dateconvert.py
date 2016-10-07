import unittest
import numpy as np
import dateconvert

class DateConversionTestCase(unittest.TestCase):
    "Test case for date conversion utility"
    def setUp(self):
        "Read in some validated MJD-ISOT pairs."
        self.test_data = np.recfromtxt('mjd_isot_test_values.txt')

    def tearDown(self):
        "Nothing to tear down."
        pass

    def test_MJD_to_ISOT(self):
        "Test conversion from MJD to ISOT."
        for mjd, isot in self.test_data:
            self.assertEqual(dateconvert.MJD_to_ISOT(mjd), isot)

    def test_ISOT_to_MJD(self):
        "Test conversion from ISOT to MJD."
        for mjd, isot in self.test_data:
            self.assertAlmostEqual(dateconvert.ISOT_to_MJD(isot), mjd, places=9)

    def test_DateConversionConsistency(self):
        "Test the round trip between MJD_to_ISOT and ISOT_to_MJD."
        for mjd in np.arange(40000, 57700, 31.1424, dtype=np.float):
            isot = dateconvert.MJD_to_ISOT(mjd)
            self.assertAlmostEqual(mjd, dateconvert.ISOT_to_MJD(isot), places=9)

    def test_ISOT_to_MJD_bad_input(self):
        "Pass the correct type (str), but with an invalid value."
        isot = '10-07-2016 00:00:00'
        self.assertRaises(ValueError, dateconvert.ISOT_to_MJD, isot)

if __name__ == '__main__':
    unittest.main()

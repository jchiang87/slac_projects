import astropy.time

def MJD_to_ISOT(mjd):
    date = astropy.time.Time(mjd, format='mjd')
    date.format = 'isot'
    return date.value

def ISOT_to_MJD(isot):
    date = astropy.time.Time(isot, format='isot')
    date.format = 'mjd'
    return date.value

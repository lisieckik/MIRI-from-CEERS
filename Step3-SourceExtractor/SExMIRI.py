from subprocess import Popen, PIPE

detectionImage = 'reprojected_HST_to_MIRI1_770.fits'
fits_file = 'MIRI770_bg_sub.fits'
rmsFile = 'MIRI770_rms.fits'
output = 'MIRI1_770_catalog.fits'

process = ['source-extractor ',
           '%s ' %detectionImage,
          '%s[1] ' %fits_file,
          '-c default.sex ',
          '-WEIGHT_IMAGE %s '%rmsFile,
          '-CATALOG_NAME %s'%output]

process = Popen(''.join(process), stdout=PIPE, stderr=PIPE, shell = True)
stdout, stderr = process.communicate()
print(stdout, stderr)


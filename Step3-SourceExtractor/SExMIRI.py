from subprocess import Popen, PIPE

# Input files
# HST reprojected detection image
detectionImage = 'reprojected_HST_to_MIRI1_770.fits'
# MIRI background substracted image
fits_file = 'MIRI770_bg_sub.fits'
# MIRI background rms image
rmsFile = 'MIRI770_rms.fits'

# Output file name
output = 'MIRI1_770_catalog.fits'


# Parameters for source extractor
process = ['source-extractor ',  # Calling the dource extractor, if you installed it manaully, change to 'sex'
           '%s ' %detectionImage,
          '%s[1] ' %fits_file,
          '-c default.sex ', 
          '-WEIGHT_IMAGE %s '%rmsFile,
          '-CATALOG_NAME %s'%output]

# Calling procces in bash
# If you want, you can call it from termianl, just write here print(''.join(process))
# And copy result to terminal
process = Popen(''.join(process), stdout=PIPE, stderr=PIPE, shell = True)
stdout, stderr = process.communicate()
print(stdout, stderr)


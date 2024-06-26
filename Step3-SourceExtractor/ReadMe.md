# Photometry extraction
Now finally we will extract JWST fluxes from images. For this purpose we will use SourceExtractor code. In this example I am using the version installed via ```apt-get```. If you installed it manually, you need to change in code the line xxx from ```source-extractor``` to ```sex```. 

## Required files
For the extraction we need, obiously, the image we are going to extract from. In this case it is MIRI1 770 background substracted file from previous step. To evaluate teh errors we will need the rms file, also from previous step. Additionally, since we use double image mode, we need the detection image. In this case the reprojected HST file from step 1. Finally, since SourceExtractor is a widely used software, it requires some of additional files:
- default.sex - this is configuration file, here you are going to change the input and most important parameters
- default.param - this is the output-handle file, here you are going to change what will be saved in the final catalog (eg. position, size, flux, eccenticity)
- default.psf - this is point spread function file, once you will get more advanced with SEx, you will learn how to proceed with that
- default.conv

All of them can be downloaded [here](https://github.com/astromatic/sextractor/tree/master/config). 

## Default.sex
Let's modify the config file:
- line 8, change from FITS_LDAC to FITS_1.0
- line 15m change from 2 to 10, it will help you not detecting artifacts
- line 16 (17), change 1.5 (2) to 1.1 (1.1), it will allow you to detect fainter sources
- line 20, change from gauss_4.0_7x7.conv to default.conv, we are going to use the default file
- line 31, change from NONE to NONE, MAP_RMS, as we are using double image mode, we need to specify two files, but we dont care about errors of the HST detection image, so we wont give it
- line 42, change 0.0 to 25.70091, this is for scaling, each observation has its own zeropoint
- line 45, change 1.0 to 0, our file has size information
- line 49, change from 1.2 to 0.5, our data is high-quality

All the other lines are also important, but you will learn how to use them as you will get experience with source extractor.
## Default.param
It is worth to add three lines to this file:
- ALPHA_J2000     (This is rectascension)
- DELTA_J2000     (This is declination)
- MAGERR_AUTO     (This is the error)

## SExMIRI.py
In this code I show you how to call source extractor using python. It can be easily automitized using loops.

# You did it!
You now have extracted photometry. The first task to check if it was worth is to compare it to the Yang catalog. Let me know if you need some help with that (you gonna need to change from magnitudes to Jansky)!
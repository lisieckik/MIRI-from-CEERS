# Photometry extraction
Now finally we will extract JWST fluxes from images. For this purpose we will use SourceExtractor code. In this example I am using the version installed via ```apt-get```. If you installed it manually, you need to change in code the line xxx from ```source-extractor``` to ```sex```. 

## Required files
For the extraction we need, obiously, the image we are going to extract from. In this case it is MIRI1 770 file. Additionally, since we use double image mode, we need the detection image. In this case the reprojected HST file from previous step. Finally, since SourceExtractor is a widely used software, it requires some of additional files:
- default.sex - this is configuration file, here you are going to change the input and most important parameters
- default.param - this is the output-handle file, here you are going to change what will be saved in the final catalog (eg. position, size, flux, eccenticity)
- default.psf - this is point spread function file, once you will get more advanced with SEx, you will learn how to proceed with that

All of them can be downloaded [here](https://github.com/astromatic/sextractor/tree/master/tests). 
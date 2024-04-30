# Reproject and crop
Here we are going to prepare HST file for further analysis. JWST MIRI image is 1500x1500 pixels with pixel size 0.09 arcsec, while HST image is 81600x25200 pixels with 0.03 arcsec pixel size (you can check that in headers). We need to match not only the area of sky obserwed by JWST to HST image, but also the size of the pixels.

## miriSizeMatch.py
Here I prepared the code which does this process for you. You just need to run it having both HST and JWST images downloaded in previous step in the same directory as the code. I suggest you at least take a look at the code. It is commented.
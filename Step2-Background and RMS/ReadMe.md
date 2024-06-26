# Background
Each observation is a sum of the real flux and a noise. In the case of high-quality JWST data, usually the instrumental noise is reduced, so we have to check only for the physical noise, the background. We are going to estimate the background impact, calculate its root mean square (RMS) and substract it from science image. All three parts are done in the code in this directiory. The example from photoutils can be found [here](https://photutils.readthedocs.io/en/stable/background.html).

## rmsAndBackground.py
Here I prepared the code, which takes you through the process. It takes only one input. As a result you get two new files, 'MIRI770_rms.fits' and 'MIRI770_bg_sub.fits'.


from astropy.stats import SigmaClip
from photutils.background import Background2D, MedianBackground, MeanBackground
import os
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np


def make_RMS_bg(big_image, rms_output_name, SCI_bks_name, dx = 50, dy = 50):
    """
    :param big_image: Input file, background will be build on that
    :param rms_output_name: Name of the output RMS file
    :param SCI_bks_name: Name of the output background substracted image
    :param dx: Size of the RMS box in x axis
    :param dy: Size of the RMS box in y axis
    :return:
    """
    # Opening the file
    hdu = fits.open(big_image)
    # Reading the data. We use hdul index 1 because if you check in the CEERS readme file
    # it refers to image before background substraction
    data = hdu[1].data

    # Coverage mask deletes the pixels without data from rms estimation
    coverage_mask = data==0
    # Reading header
    header = hdu[1].header

    # Building the background file using the usual photoutils function
    # If you want to know the details check the documentation
    # In short, it cutouts every peak (source) in the data and building the background over the rest of pixels
    # The size of dx and dy should be big enought to cover extended sources
    # Filter smoothes the result background
    zerr = Background2D(data,
                        (dx, dy),
                        sigma_clip=clip,
                        filter_size=(5,5),
                        bkg_estimator=bgEstimator,
                        coverage_mask = coverage_mask,
                        fill_value = 0)

    # Here we save the rms map
    fits.writeto(rms_output_name,zerr.background_rms, header=header,
                 overwrite=True)
    # Here we save the background substracted map
    fits.writeto(SCI_bks_name,data-zerr.background, header=header,
                 overwrite=True)  # writing the cutout data to a new fits file with the output filename given above

# Those two objects are typically used for background estimation
# This is the method used for final values to be calculated
bgEstimator = MedianBackground()
# This is the value above which everything is counded as a source
clip = SigmaClip(sigma=3)

# Input file
Miripath = "hlsp_ceers_jwst_miri_miri1_f770w_dr0.6_i2d.fits"

make_RMS_bg(Miripath,
            'MIRI770_rms.fits',
            'MIRI770_bg_sub.fits')

from astropy.io import fits
from reproject import reproject_interp

def reproject_fits(input_fits_filename, hdu_index1, reference_fits_file, hdu_index2, old_pixel_scale_arcsec,
                   new_pixel_scale_arcsec, output_fits_filename):
    """
    :param input_fits_filename: File for reprojection (in this example HST image)
    :param hdu_index1: Index of fits extension of reprojection file
    :param reference_fits_file: File to which we will match reprojection (JWST)
    :param hdu_index2: Index of fits extension of reference file
    :param old_pixel_scale_arcsec: Linear size
    :param new_pixel_scale_arcsec: Linear size
    :param output_fits_filename: Output size
    :return: None
    """
    # Open the input FITS file, which will be reprojected
    hdul_input = fits.open(input_fits_filename)
    # Since fits files can have multiple extensions, we need to point which one we will use
    # For this purpose we use hdu_index1
    HST_Image = hdul_input[hdu_index1].data
    # For flux conversion we need to divide the data by the pixel area (original one)
    HST_Image = HST_Image/(old_pixel_scale_arcsec ** 2)
    # Since we want to keep the file as it is, we will input new, scaled data back to the file
    hdul_input[hdu_index1].data = HST_Image

    # Open the reference FITS file, the one we will match the reprojection
    hdul_reference = fits.open(reference_fits_file)


    # Here we reproject and cutout the file using standard function from the package
    # If you are interested how it works, check the documentation
    # In short, it takes old image, crop it to match the size of reference image and interpolate the values of pixels via size scaling
    # You can see, we use the header from the reference file
    # It just make it easier for further analysis
    array, footprint = reproject_interp(hdul_input[hdu_index1], hdul_reference[hdu_index2].header)

    # For flux conversion this time we have to multiply by pixel area (new one)
    array = array * (new_pixel_scale_arcsec ** 2)

    # Finally we save the reprojected file
    hdu_out = fits.PrimaryHDU(data=array, header=hdul_reference[hdu_index2].header)
    hdul_out = fits.HDUList([hdu_out])
    hdul_out.writeto(output_fits_filename, overwrite=True)

    # Close the input FITS file
    hdul_input.close()
    hdul_reference.close()


# Input files
# Path to the MIRI image file
Miripath = "/home/lisieckik/Pulpit/Darko galaxie/v2/MiriCatalogs/miri1/hlsp_ceers_jwst_miri_miri1_f770w_dr0.6_i2d.fits"
# Path to the HST image file
HSTpath = '/home/lisieckik/Pulpit/Darko galaxie/v2/HST/egs_all_wfc3_ir_f160w_030mas_v1.9_drz.fits'


reproject_fits(HSTpath,
               0,
               Miripath,
               1,
               0.03,
               0.09,
               "reprojected_HST_to_MIRI1_770.fits")

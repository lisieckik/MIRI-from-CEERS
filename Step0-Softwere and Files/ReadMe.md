# In this step we will go through all needed soft and files

First of all, you need **LINUX MACHINE** since some of softwere is written only for linux.

Following, to be able to reproduce this example you gonna need:
- Python 3.x (I suppose it should work with any version above 3.8, I use 3.10) with following packages:
    - Numpy, Matplotlib, Astropy
    - [Reproject](https://pypi.org/project/reproject/), since JWST MIRI has different pixel size than HST
    - Subprocess (I think it is default with python), it helps with automatization
- [SourceExtractor](https://sextractor.readthedocs.io/en/latest/Installing.html)
- Not necessary:
    - useful for handling the catalogs, [TopCat](https://www.star.bris.ac.uk/~mbt/topcat/)
    - usefull for cheking the images, [SAO Image DS9](https://sites.google.com/cfa.harvard.edu/saoimageds9)


### Pyhton 
I hope you are able to install python and its packages. If no, let me know, I will put here some explanation.

### Source Extractor, SEx
The easiest way is definitely to run ```apt-get sextractor``` (while on Debian, this is probably the one, but you can google it) or ```dnf sextractor``` (while on Fedora). Then you can simply call it within terminal by writing ```source-extractor```. Otherwise, it can be hard depending on machine you are using. I found it challenging to install it by downloading source code. You can try it following the [instructions](https://sextractor.readthedocs.io/en/latest/Installing.html).

Once you installed, try to call it in terminal bye writing ```source-extractor``` (if installed with apt-get) or ```sex``` (if installed via source).

## Files
### Detection Image
Now let's download the files needed for double image mode. First the detection image. We are going to use Hubble Space Telescope f160w image with matched astrometry. It can be found [here](https://ceers.github.io/hdr1.html). Just scroll down, find row WFC3/IR F160W, then column Science Image and downlowad file (fits or zip).

### Photometry Image
Finally, we can download JWST MIRI image used for further analysis. Let's start at [data release 0.6 from CEERS website.](https://ceers.github.io/dr06.html) It is worth to check [readme](https://web.corral.tacc.utexas.edu/ceersdata/DR06/NIRCam/README.txt), but we are interested in Epoch 1&2 MIRI mosaics. Just scroll down, find column MIRI1 and download file F770. At the bottom of the page you can find a link to paper Yang et al. (2023) with similar aproach to reduction. This is great, becamuse we will have a source to comparison!

Once you downloaded both files, let's take a look at them. For this purpose you can use SAO DS9. Just open the soft and find your files. It will handle fits files. It can take a while to open HST image since it is quite big. Now let's move to step 1!
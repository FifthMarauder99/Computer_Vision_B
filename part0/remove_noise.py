
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
import sys
from scipy import fftpack
import numpy as np

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        raise Exception("error: please give an input image name as a parameter, like this: \n"
                        "python3 remove_noise.py noisy_pichu.png")

    img = Image.open(sys.argv[1])

    # Current image has diagonal black white pattern noise
    # Removing that noise consists of 3 steps:
    # 1. Using min filter for smoothing diagonal black pattern
    # 2. Adding Max filter for smoothing diagonal white pattern
    # 3. Adding Gaussian filter for smooth all pixels
    denoise = img.filter(ImageFilter.MinFilter(size=7))
    denoise = denoise.filter(ImageFilter.MaxFilter(size=5))
    denoise = denoise.filter(ImageFilter.GaussianBlur(radius=2))
    denoise.save('denoise_pichu.png')

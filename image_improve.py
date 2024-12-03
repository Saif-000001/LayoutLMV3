import numpy as np
from skimage.io import imread, imsave
from skimage import exposure, img_as_ubyte
from skimage.color import rgb2gray
import os

# Ensure the output directory exists
os.makedirs('./image/', exist_ok=True)

# Load the image
image = imread('./image/img.png')  # Load the image from the specified path

# Convert to grayscale if necessary
image_gray = rgb2gray(image)

# Apply global histogram equalization
image_eq = exposure.equalize_hist(image_gray)

# Save the equalized image
imsave('./image/equalized_image.png', img_as_ubyte(image_eq))  # Save as 8-bit image
print("Equalized image saved successfully at './image/equalized_image.png'.")

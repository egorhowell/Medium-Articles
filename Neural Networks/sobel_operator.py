# Import packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

# Input image
image = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200]
])

# Sobel Operators
G_x = np.array([
    [-1, 0, +1],
    [-2, 0, +2],
    [-1, 0, +1]
])

G_y = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [+1, +2, +1]
])

# Apply the Sobel kernels to the image
output_x = ndimage.convolve(image.astype(float), G_x)
output_y = ndimage.convolve(image.astype(float), G_y)

# Define the light grey color for the background
light_grey = [0.8, 0.8, 0.8]  # RGB values for light grey

# Normalize the Sobel outputs
norm_output_x = (output_x - output_x.min()) / (output_x.max() - output_x.min())
norm_output_y = (output_y - output_y.min()) / (output_y.max() - output_y.min())

# Set the background color of the plots
plt.rcParams['figure.facecolor'] = light_grey
plt.rcParams['axes.facecolor'] = light_grey

# Plot the images with the light grey background
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(image, cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(norm_output_x, cmap='gray')
axes[1].set_title('Sobel - Horizontal Direction')
axes[1].axis('off')

axes[2].imshow(norm_output_y, cmap='gray')
axes[2].set_title('Sobel - Vertical Direction')
axes[2].axis('off')

plt.tight_layout()
plt.show()

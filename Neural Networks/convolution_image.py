import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

# Original image
image = np.array([
    [10, 10, 10, 10, 10],
    [10, 30, 30, 30, 10],
    [10, 30, 70, 30, 10],
    [10, 30, 30, 30, 10],
    [10, 10, 10, 10, 10]
])

# Kernel
kernel = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]) / 9

# Convolution
result = convolve2d(image, kernel, mode='same', boundary='fill', fillvalue=0)

# Plotting
plt.figure(figsize=(10, 5))

# Original Image
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Input Image')
plt.axis('off')

# Convolved Image
plt.subplot(1, 2, 2)
plt.imshow(result, cmap='gray')
plt.title('Output Image')
plt.axis('off')

plt.show()
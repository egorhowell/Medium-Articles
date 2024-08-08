# Import packages
import matplotlib.pyplot as plt
import numpy as np

# Define the size of the image and create a black canvas
size = 20
flower_image = np.zeros((size, size))

# Draw a simple flower pattern
center = size // 2
radius_outer = size // 4
radius_inner = size // 8


# Function to check if a point is inside a circle
def is_in_circle(x, y, center_x, center_y, radius):
    return (x - center_x) ** 2 + (y - center_y) ** 2 < radius**2


# Fill in the pixels for the petals and inner circle
for x in range(size):
    for y in range(size):
        if is_in_circle(x, y, center, center, radius_outer):
            flower_image[x, y] = 255  # white
        if is_in_circle(x, y, center, center, radius_inner):
            flower_image[x, y] = 100  # gray

# Plots
fig, axs = plt.subplots(1, 2, figsize=(15, 7), gridspec_kw={"width_ratios": [1, 1]})

axs[0].imshow(flower_image, cmap="gray", interpolation="nearest")
axs[0].set_title("Grayscale Flower Image")
axs[0].axis("off")  # Hide the axis for the image

axs[1].set_xlim(-0.5, size - 0.5)
axs[1].set_ylim(-0.5, size - 0.5)
axs[1].set_xticks(np.arange(size) - 0.5, minor=True)
axs[1].set_yticks(np.arange(size) - 0.5, minor=True)
axs[1].grid(which="minor", color="black", linestyle="-", linewidth=2)
axs[1].tick_params(which="minor", size=0)

for (i, j), value in np.ndenumerate(flower_image):
    axs[1].text(j, i, int(value), ha="center", va="center", color="black", fontsize=8)

# Hide the major ticks and labels
axs[1].tick_params(
    which="major", bottom=False, left=False, labelbottom=False, labelleft=False
)
axs[1].set_title("Pixel Values Grid")

plt.tight_layout()
plt.show()

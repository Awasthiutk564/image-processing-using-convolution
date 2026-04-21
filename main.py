import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read image
image = cv2.imread('image.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #type: ignore

# Blur kernel
blur_kernel = np.ones((3,3), np.float32) / 9
blurred = cv2.filter2D(image_rgb, -1, blur_kernel)

# Sharpen kernel
sharpen_kernel = np.array([[0,-1,0],
                           [-1,5,-1],
                           [0,-1,0]])
sharpened = cv2.filter2D(image_rgb, -1, sharpen_kernel)

# Edge Detection kernel
edge_kernel = np.array([[-1,-1,-1],
                        [-1, 8,-1],
                        [-1,-1,-1]])

edges = cv2.filter2D(image_rgb, -1, edge_kernel)

# Save outputs
cv2.imwrite("blurred_output.jpg", cv2.cvtColor(blurred, cv2.COLOR_RGB2BGR))
cv2.imwrite("sharpened_output.jpg", cv2.cvtColor(sharpened, cv2.COLOR_RGB2BGR))
cv2.imwrite("edge_output.jpg", cv2.cvtColor(edges, cv2.COLOR_RGB2BGR))

# Display
plt.figure(figsize=(18,5))

plt.subplot(1,4,1)
plt.imshow(image_rgb)
plt.title("Original")
plt.axis('off')

plt.subplot(1,4,2)
plt.imshow(blurred)
plt.title("Blurred")
plt.axis('off')

plt.subplot(1,4,3)
plt.imshow(sharpened)
plt.title("Sharpened")
plt.axis('off')

plt.subplot(1,4,4)
plt.imshow(edges)
plt.title("Edges")
plt.axis('off')

plt.show()
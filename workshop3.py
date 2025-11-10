import cv2
import matplotlib.pyplot as plt

# Step 1: Read the image
img = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

# Step 2: Apply Gaussian Blur to remove noise
blur = cv2.GaussianBlur(img, (5,5), 1.4)

# Step 3: Apply Canny Edge Detection
edges = cv2.Canny(blur, threshold1=100, threshold2=200)

# Step 4: Display the original and edge images
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')

plt.subplot(1,2,2)
plt.title("Canny Edges")
plt.imshow(edges, cmap='gray')

plt.show()
```
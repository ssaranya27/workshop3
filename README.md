# WORKSHOP 3-Canny Edge Detection

### **AIM**

To implement the **Canny Edge Detection algorithm** using Python and OpenCV on a sample image to detect and analyze edges.


### **APPARATUS / SOFTWARE REQUIRED**

* Python 3.x
* OpenCV library (`cv2`)
* Matplotlib library
* A sample image file (`.jpg` or `.png`)

---

### **PROCEDURE**

1. **Import Libraries:**
   Import the necessary modules — OpenCV for image processing and Matplotlib for displaying images.

2. **Read the Image:**
   Load the input image using `cv2.imread()` and convert it to grayscale for edge detection.

3. **Noise Reduction (Gaussian Blur):**
   Apply a Gaussian filter to smooth the image and reduce noise that might cause false edges.

4. **Apply Canny Edge Detection:**
   Use the `cv2.Canny()` function with suitable threshold values to detect edges.

5. **Display the Results:**
   Show both the original and edge-detected images using Matplotlib.
### ** PROGRAM **
```
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
### ** OUTPUT**

 <img width="1485" height="695" alt="image" src="https://github.com/user-attachments/assets/1032acbf-cbde-40d9-8960-182e4dbf69c7" />


### **RESULT**

The **Canny Edge Detection algorithm** successfully identified edges in the sample image. By tuning the threshold parameters, the clarity and number of detected edges can be adjusted.

---

Would you like me to format it as a short “lab record page” (with sections like *Theory*, *Algorithm*, *Output*, etc.) so it looks ready to print?

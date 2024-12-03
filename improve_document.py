import cv2

# Load the image
image = cv2.imread('./image/img.png')

# Check if the image is loaded
if image is None:
    print("Image not found. Check the file path.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding
binary = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)

# Convert to uint8 if needed
binary = binary.astype('uint8')

# Remove noise
denoised = cv2.fastNlMeansDenoising(binary, None, 30, 7, 21)

# Save the processed image
cv2.imwrite('./image/img_1.png', denoised)
print("Image processed and saved as img_1.png")

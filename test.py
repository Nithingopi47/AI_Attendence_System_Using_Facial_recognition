import cv2
import face_recognition

def test_image(file_path):
    img = cv2.imread(file_path, cv2.IMREAD_COLOR)  # Force read as color image
    if img is not None:
        print(f"Image shape: {img.shape}")  # Print image dimensions
        print(f"Image dtype: {img.dtype}")   # Print image data type
        print(f"Image channels: {img.shape[2]}")  # Print number of channels
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        try:
            encodings = face_recognition.face_encodings(img_rgb)
            if encodings:
                print("Encoding successful")
            else:
                print("No face found")
        except Exception as e:
            print(f"Error during face encoding: {e}")
    else:
        print("Error loading image")

# Use raw string literals or forward slashes
test_image(r'D:\\Files\\Images\\1SP21CS006.png')

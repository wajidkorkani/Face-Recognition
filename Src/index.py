import cv2
import face_recognition

# -------- Step 1: Capture a picture from the camera --------
cap = cv2.VideoCapture(0)

ret, frame = cap.read()  # Take one picture
if not ret:
    print("Failed to grab frame")
    cap.release()
    exit()

# Save captured image
captured_path = "captured.jpg"
cv2.imwrite(captured_path, frame)

cap.release()
cv2.destroyAllWindows()

# -------- Step 2: Compare with known images --------
images = [
    "one.jpg", 
    "two.jpg", 
    "three.jpg", 
    "four.jpg", 
    "five.jpg", 
    "six.jpg", 
    "seven.jpg",
    "eight.jpg",
    "nine.jpg",
    "ten.jpg",
    "eleven.jpg",
]

i = 0

# Load known and unknown images
unknown_image = face_recognition.load_image_file(captured_path)

while(i < len(images)):
    known_image = face_recognition.load_image_file(images[i])
    
    # Encode faces
    known_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    
    # Compare faces
    results = face_recognition.compare_faces([unknown_encoding], known_encoding)
    
    if results[0]:
        print(f"Image {images[i]} matches the unknown image.")
        i = len(images)  # Exit loop if a match is found
    
    i += 1
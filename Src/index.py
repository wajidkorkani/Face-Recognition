import cv2
import face_recognition
import os

# -------- Step 1: Capture a picture from the camera --------
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if not ret:
    print("Failed to grab frame")
    cap.release()
    exit()

cv2.imshow("Laptop Camera", frame)
captured_path = "captured.jpg"
cv2.imwrite(captured_path, frame)
cap.release()
cv2.destroyAllWindows()

# -------- Step 2: Compare with known images --------
images = [
    "one.jpg", "two.jpg", "three.jpg", "four.jpg", "five.jpg", "six.jpg",
    "seven.jpg", "eight.jpg", "nine.jpg", "ten.jpg", "eleven.jpg", "13.jpg"
]

# Load unknown image
unknown_image = face_recognition.load_image_file(captured_path)
unknown_encodings = face_recognition.face_encodings(unknown_image)

if not unknown_encodings:
    print("❌ No face found in captured image!")
    exit()

unknown_encoding = unknown_encodings[0]

# Loop through known images
for img_name in images:
    if not os.path.exists(img_name):
        print(f"⚠ File {img_name} not found, skipping...")
        continue

    known_image = face_recognition.load_image_file(img_name)
    known_encodings = face_recognition.face_encodings(known_image)

    if not known_encodings:
        print(f"⚠ No face found in {img_name}, skipping...")
        continue

    known_encoding = known_encodings[0]
    results = face_recognition.compare_faces([known_encoding], unknown_encoding)

    if results[0]:
        print(f"✅ Match found: {img_name}")
        break
else:
    print("❌ No match found.")

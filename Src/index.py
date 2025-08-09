import cv2
import face_recognition
import time

# -------- Step 1: Open camera for 10 seconds --------
cap = cv2.VideoCapture(0)

start_time = time.time()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    cv2.imshow("Laptop Camera", frame)
    
    # If 10 seconds passed, break and save frame
    if time.time() - start_time >= 10:
        captured_path = "captured.jpg"
        cv2.imwrite(captured_path, frame)
        print("Picture taken and saved as captured.jpg")
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

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
    "13.jpg",
]

# Load captured image
unknown_image = face_recognition.load_image_file(captured_path)
unknown_encodings = face_recognition.face_encodings(unknown_image)

if not unknown_encodings:
    print("No face found in captured image.")
    exit()

unknown_encoding = unknown_encodings[0]

# Compare with each known image
for img_name in images:
    known_image = face_recognition.load_image_file(img_name)
    known_encodings = face_recognition.face_encodings(known_image)

    if not known_encodings:
        print(f"No face found in {img_name}")
        continue

    known_encoding = known_encodings[0]
    results = face_recognition.compare_faces([known_encoding], unknown_encoding)

    if results[0]:
        print(f"Image {img_name} matches the captured image.")
        break

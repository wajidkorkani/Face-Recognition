import face_recognition

# Load known and unknown images
known_image = face_recognition.load_image_file("one.jpg")
unknown_image = face_recognition.load_image_file("eleven.jpg")

# Encode faces
known_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

# Compare faces
results = face_recognition.compare_faces([known_encoding], unknown_encoding)
print("Match found:", results[0])

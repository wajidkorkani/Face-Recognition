import face_recognition

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
    "twelve.jpg"
    ]

i = 0

# Load known and unknown images
known_image = face_recognition.load_image_file("four.jpg")

while(i < len(images)):
    unknown_image = face_recognition.load_image_file(images[i])
    
    # Encode faces
    known_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    
    # Compare faces
    results = face_recognition.compare_faces([known_encoding], unknown_encoding)
    
    if results[0]:
        print(f"Image {images[i]} matches the known image.")
        i = len(images)  # Exit loop if a match is found
    
    i += 1
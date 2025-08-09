# Face-Scanner-in-python
# Face Recognition Project

This project is a simple face recognition system using Python, OpenCV, and the `face_recognition` library. It captures an image from your webcam, then compares the captured face to a set of known images to identify the person.

## Features
- Captures a photo from your webcam after 10 seconds
- Compares the captured face with known images of famous personalities
- Prints the name of the matched person or notifies if no match is found

## How It Works
1. **Capture Image:**
	- The script opens your webcam and displays the video feed.
	- After 10 seconds, it captures a frame and saves it as `captured.jpg`.
2. **Load Known Images:**
	- The script loads a set of known images (Elon Musk, Mark Zuckerberg, Bill Gates, Jeff Bezos) from the `Src` folder.
3. **Face Recognition:**
	- The captured image is compared with each known image using the `face_recognition` library.
	- If a match is found, the name is printed; otherwise, it reports no match.

## Project Structure
```
Face-Recognition/
│
├── README.md
└── Src/
	 ├── index.py           # Main script
	 ├── captured.jpg       # Captured image from webcam (generated at runtime)
	 ├── one.jpg            # Known images (Elon Musk)
	 ├── two.jpg
	 ├── three.jpg          # Known images (Mark Zuckerberg)
	 ├── four.jpg
	 ├── five.jpg
	 ├── six.jpg
	 ├── seven.jpg          # Known images (Bill Gates)
	 ├── ten.jpg
	 ├── eleven.jpg
	 ├── eight.jpg          # Known images (Jeff Bezos)
	 └── nine.jpg
```

## Requirements
- Python 3.6+
- OpenCV (`opencv-python`)
- face_recognition

## Installation
1. Clone the repository or download the source code.
2. Install the required packages:
	```powershell
	pip install opencv-python face_recognition
	```
3. Place the known images in the `Src` folder as shown above.

## Usage
1. Run the main script:
	```powershell
	cd Src
	python index.py
	```
2. The webcam will open. After 10 seconds, a photo will be taken and compared with the known images.
3. The result will be printed in the terminal.

## Notes
- Press `q` to quit the webcam window early.
- Make sure your webcam is connected and accessible.
- You can add more known images by updating the `images` dictionary in `index.py`.


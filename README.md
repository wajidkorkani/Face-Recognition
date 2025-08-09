
# Face Recognition in Python

## Overview
This project is a simple face recognition system using Python, OpenCV, and the `face_recognition` library. It captures an image from your webcam and compares it to a set of known images to identify the person. The project is intended for learning and demonstration purposes.

## Features
- Captures a photo from your webcam after 10 seconds
- Compares the captured face with known images (Elon Musk, Mark Zuckerberg, Bill Gates, Jeff Bezos)
- Prints the name of the matched person or notifies if no match is found

## How It Works
1. The script opens your webcam and displays the video feed.
2. After 10 seconds, it captures a frame and saves it as `captured.jpg`.
3. The script loads a set of known images from the `Src` folder.
4. The captured image is compared with each known image using the `face_recognition` library.
5. If a match is found, the name is printed; otherwise, it reports no match.

## Project Structure
```
Face-Recognition/
│   LICENSE
│   README.md
└───Src/
	│   index.py
	│   one.jpg
	│   two.jpg
	│   three.jpg
	│   four.jpg
	│   five.jpg
	│   six.jpg
	│   seven.jpg
	│   eight.jpg
	│   nine.jpg
	│   ten.jpg
	│   eleven.jpg
	└── captured.jpg (generated at runtime)
```

## Requirements
- Python 3.6 or higher
- OpenCV (`opencv-python`)
- face_recognition

## Installation
1. Clone or download this repository.
2. Install the required packages:
	```powershell
	pip install opencv-python face_recognition
	```
3. Place the known images in the `Src` folder as shown above.

## Usage
1. Open a terminal and navigate to the `Src` directory:
	```powershell
	cd Src
	```
2. Run the main script:
	```powershell
	python index.py
	```
3. The webcam will open. After 10 seconds, a photo will be taken and compared with the known images. The result will be printed in the terminal.

## Extending the Project
- To add more known faces, add their images to the `Src` folder and update the `images` dictionary in `index.py`.
- You can use any image file name, just ensure it matches the dictionary entry.

## Troubleshooting
- **No face found in captured image:** Ensure your face is clearly visible to the webcam and there is enough lighting.
- **No face found in known images:** Make sure the known images are clear and contain only one face.
- **Webcam not detected:** Check your webcam connection and permissions.
- **Missing dependencies:** Reinstall required packages with `pip install opencv-python face_recognition`.

## License
MIT License. See the [LICENSE](LICENSE) file for details.

## Author
Abdul Wajid Korkani


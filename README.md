# Avatar.ai - Virtual Trial Room

Avatar.ai is a web-based virtual trial room application that allows users to upload images and try on clothes virtually. The app uses computer vision techniques to detect human poses and overlay clothing items onto the user's image, creating a virtual try-on experience.

## Features

- **Image Upload**: Upload an image of yourself to the app.
- **Clothing Selection**: Choose a clothing item from a list of predefined options.
- **Virtual Try-On**: The app uses pose detection to overlay the selected clothing item onto your image.
- **Output**: The final image with the clothing overlay is generated and provided for download.

## Tech Stack

- **Flask**: Web framework for building the web application.
- **OpenCV**: Library for computer vision tasks such as image processing and pose detection.
- **cvzone**: Python library for computer vision tasks, used for pose detection and image overlay.
- **Werkzeug**: Utility library for secure file handling.
- **HTML/CSS/JavaScript**: For front-end design.

## Requirements

Before running the project, make sure you have the following libraries installed:

- Python 3.x
- Flask
- OpenCV
- cvzone
- Werkzeug

You can install the necessary dependencies using the following command:

```bash
pip install flask opencv-python cvzone werkzeug

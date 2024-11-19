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
pip install requirements.txt
```

# How to Run

1. **Clone the repository**:

    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```

2. **Ensure the required images are placed in the correct directories**:
    - Clothing images should be placed in the `static/used/` folder (e.g., `1.PNG`, `2.PNG`, etc.).
    - Uploaded images will be saved in the `static/uploads/` folder.

3. **Run the Flask application**:

    ```bash
    python app.py
    ```

4. Open your browser and navigate to `http://localhost:5001` to access the virtual trial room.

## Project Structure

├── app.py                 # Main Flask application
├── static/
│   ├── uploads/           # Folder for uploaded images
│   └── used/              # Folder for clothing images
├── templates/
│   └── render.html        # HTML template for the upload page
├── requirements.txt       # Python dependencies
└── README.md              # This file


## File Upload
- The app allows users to upload images through a form.
- The uploaded image is saved in the `static/uploads/` folder.

## Clothing Selection
- The user selects a clothing item from a set of predefined options (e.g., `cloth1`, `cloth2`, etc.).
- The selected clothing item is loaded from the `static/used/` folder.

## Pose Detection
- The app uses `cvzone`'s PoseDetector to detect the user's pose and position.
- Clothing items are resized based on the user's body proportions to fit correctly.

## Output
- The resulting image, with the clothing overlayed, is saved as `output.png` and displayed for download.

## Notes
- Ensure that the uploaded image clearly shows the user’s body for accurate pose detection.
- The app currently supports only a limited set of clothing images.
- The clothing overlay will only work properly if the pose detection returns enough body landmarks.



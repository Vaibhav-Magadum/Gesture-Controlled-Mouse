# Hand Gesture Controlled Presentation

This project allows you to control your computer's mouse and presentation slides using hand gestures. The system uses a webcam to detect hand gestures and translates them into mouse movements and clicks. The project utilizes OpenCV for video capture, MediaPipe for hand landmark detection, and PyAutoGUI for controlling the mouse and keyboard.

## Features

- **Mouse Movement**: Control the mouse cursor with the tip of your index finger.
- **Click**: Perform a mouse click when the index finger and thumb tips come close together.
- **Presentation Control**: Navigate through presentation slides using gestures (swipe gestures to be implemented).

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI

## Installation

1. **Install Python**: Make sure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Packages**: Open a terminal or command prompt and run the following commands:

    ```bash
    pip install opencv-python mediapipe pyautogui
    ```

## Usage

1. **Clone or Download the Repository**:

    If you are using Git, clone the repository:
    ```bash
    git clone https://github.com/yourusername/hand-gesture-presentation-control.git
    ```

    Alternatively, download the project as a ZIP file and extract it.

2. **Run the Script**:

    Navigate to the project directory and execute the script:

    ```bash
    python hand_gesture_presentation.py
    ```

3. **Control the Presentation**:

    - **Move Mouse Cursor**: Move your index finger to control the mouse cursor.
    - **Click**: Bring your thumb and index finger tips close together to perform a click.
    - **Navigate Slides**: Swipe gestures (to be implemented) for next and previous slides.

## Code Explanation

The script `hand_gesture_presentation.py` performs the following tasks:

1. **Initialize Video Capture**: Captures video from the webcam.
2. **Initialize MediaPipe Hands**: Detects hand landmarks using MediaPipe.
3. **Capture and Process Frames**: Continuously captures frames, detects hand landmarks, and processes them.
4. **Mouse Control**: Moves the mouse cursor based on the position of the index finger.
5. **Click Detection**: Performs a click action when the index finger and thumb are close together.
6. **Display Frames**: Shows the video feed with landmarks drawn.




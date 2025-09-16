# Real-Time Color Detection
A Python application that detects and tracks specific colors (Yellow, Red, Blue) in real-time using computer vision. The program captures video from your webcam and draws bounding rectangles around detected colored objects.

## Description
This project uses OpenCV and PIL to perform real-time color detection through HSV color space conversion. The application can simultaneously detect multiple colors and highlight them with colored bounding boxes. It's designed to be lightweight and efficient for real-time processing.

## Features
 - Multi-color detection: Detects yellow, red, and blue objects simultaneously
 - Real-time processing: Live video feed with instant color detection
 - Visual feedback: Colored bounding rectangles around detected objects
 - Optimized HSV ranges: Tuned color ranges for better detection accuracy
 - Easy to extend: Simple structure to add more colors

## Installation Procedure

**Prerequisites**
 - Python 3.7 or higher
 - Webcam/Camera connected to your system

1. **Clone this repository**
```bash
git clone https://github.com/zidanlf/color-detection.git
cd color-detection
```

2. **Create virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
3. **Install dependencies**
```Bash
pip install -r requirements.txt
```
## How to Run
Run the main script:
```Bash
python main.py
```
Press 'q' to close the webcam window.

## How the Code Works

This project uses **OpenCV**, **NumPy**, and **Pillow (PIL)** to detect specific colors (red, yellow, and blue) from a webcam feed. The workflow is executed step by step as follows:

### 1. Initialize Target Colors
At the beginning of `main.py`, a dictionary named `colors` is defined. It contains the target colors along with their BGR values and the bounding box color to be drawn around detected objects.

```python
colors = {
    "yellow": ([0, 255, 255], (0, 255, 255)),
    "red": ([0, 0, 255], (0, 0, 255)),
    "blue": ([255, 0, 0], (255, 0, 0))
}
```
The first tuple is the BGR value of the target color, and the second tuple defines the color of the bounding box rectangle.

### 2. Open Webcam
The webcam is accessed using OpenCV’s VideoCapture. The parameter 0 refers to the default system camera. Each frame is read continuously inside a while loop.
```python
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
```
Here, frame contains the image captured from the webcam, which will then be processed.

### Convert Frame to HSV
By default, OpenCV uses the BGR color space, which is less suitable for color detection under varying lighting conditions. Therefore, each frame is converted into the HSV (Hue, Saturation, Value) color space for more reliable detection.
```python
hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
```

### 4. Get HSV Limits from utils.py
The helper function get_limits() in utils.py defines HSV thresholds for each target color. This function returns two NumPy arrays:
 - lowerLimit: the minimum HSV values for the color.
 - upperLimit: the maximum HSV values for the color.

Example for red:
```python
if name == "red":
    lowerLimit = np.array([0, 150, 120], dtype=np.uint8)
    upperLimit = np.array([2, 255, 255], dtype=np.uint8)
```
This ensures that only pixels within this HSV range are considered as red.

### 5. Create a Color Mask
For each frame, a binary mask is generated using cv2.inRange(). This mask isolates the target color from the rest of the image.
```python
colors = {
    "yellow": ([0, 255, 255], (0, 255, 255)),
    "red": ([0, 0, 255], (0, 0, 255)),
    "blue": ([255, 0, 0], (255, 0, 0))
}
```
 - Pixels within the HSV range appear white (255).
 - Pixels outside the range appear black (0).
The mask highlights only the regions containing the target color.

### 6. Find Bounding Box
The mask is converted into a Pillow image so that the bounding box of the detected color region can be calculated.
```python
mask_ = Image.fromarray(mask)
bbox = mask_.getbbox()
```
 - If a color region exists, bbox returns coordinates (x1, y1, x2, y2).
 - If no color is detected, bbox = None.

### 7. Draw Bounding Box on the Frame
If a bounding box is found, a rectangle is drawn on the original frame to highlight the detected object.
```python
frame = cv2.rectangle(frame, (x1, y1), (x2, y2), box_color, 3)
```
 - (x1, y1) is the top-left corner of the rectangle.
 - (x2, y2) is the bottom-right corner.
 - box_color defines the rectangle color (same as the detected color).
 - 3 specifies the thickness of the rectangle border.

### 8.Display the Result in Real-Time

The processed frame with bounding boxes is displayed in a window named 'frame'.
```python
cv2.imshow('frame', frame)
```
The display updates continuously, showing detections in real time.

### 9.Exit the Program
The program runs in a loop until the user presses the q key. Once pressed, the loop breaks, the webcam is released, and all OpenCV windows are closed.
```python
if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
```
## Video
Youtube: https://youtu.be/3zAxGH3avLM

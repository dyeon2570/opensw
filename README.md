# ARE YOU HAPPY? #
---
## Project Overview<br>
### This project aims to develop a real-time system for detecting faces and analyzing emotions using open-source libraries Mediapipe and Hugging Face.
### The system processes video input from a webcam, detects faces, and displays emotion analysis results in real time.
---
## Features<br>
- ### Real-Time Face Detection: Uses Mediapipe to detect faces in a live video feed.
- ### Emotion Recognition: Predicts the emotion of the detected face using a Hugging Face sentiment analysis pipeline.
- ### Interactive Interface: Displays the live video feed with bounding boxes and emotion labels for detected faces.<br>
---

## Code Overview
1. Dependencies:
* opencv-python: Captures video and displays the output.
* mediapipe: Detects faces in the video feed.
* transformers: Provides the Hugging Face sentiment analysis pipeline.

2. Key Components:
* Face Detection: Mediapipe detects faces and extracts bounding box information.
* Emotion Prediction: Hugging Face's sentiment analysis pipeline predicts emotion using predefined text.

3. Visualization:
* Bounding boxes are drawn around detected faces.
* Emotion labels and confidence scores are displayed above each face.






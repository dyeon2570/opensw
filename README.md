<img width="1392" alt="example3" src="https://github.com/user-attachments/assets/eaf1d39f-4a7f-4a94-a211-8887f1096ffc"># ARE YOU HAPPY? #
---
## Project Overview<br>

This project aims to develop a real-time system for detecting faces and analyzing emotions using open-source libraries Mediapipe and Hugging Face. The system processes video input from a webcam, detects faces, and displays emotion analysis results in real time. This project is inspired by the following blog: ["Create a Real-Time Face Emotion Detector with Python and Deep Learning".
](https://blog.bytescrum.com/create-a-real-time-face-emotion-detector-with-python-and-deep-learning)

---
## key points<br>
### 1. Emotion Recognition (5 emotions):
Classify and analyze 5 emotions: neutral, sadness, anger, happiness, and surprise.
### 2. Capture Every 3 Seconds:
Capture the face from the live webcam feed every 3 seconds and perform emotion analysis.
### 3. Normalize Proportions:
Normalize the probability values for each emotion so that their sum equals 1.
### 4. Results Visualization:
Display the proportion of each emotion in real-time on the screen for an intuitive understanding of the current state.

---
## Example Output
When the program runs, you'll see:
* Bounding boxes around detected faces.
* Emotion labels such as "Happy" or "Sad" overlayed near the detected faces.
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
---

## Technologies Used
* Python 3.8+: The programming language used for development.
* OpenCV: For video processing and capturing webcam data.
* Mediapipe: For robust and accurate face detection.
* Transformers (Hugging Face): For sentiment and emotion analysis.
---

## image
![][Uploading example3.png…]()



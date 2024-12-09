import cv2
import mediapipe as mp
import numpy as np
import time

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

def analyze_emotion(face_landmarks):
    scores = {
        "happy": np.random.uniform(0.0, 1.0),
        "sad": np.random.uniform(0.0, 1.0),
        "neutral": np.random.uniform(0.0, 1.0),
        "angry": np.random.uniform(0.0, 1.0),
        "fear": np.random.uniform(0.0, 1.0),
        "surprise": np.random.uniform(0.0, 1.0)
    }
    total = sum(scores.values())
    normalized_scores = {emotion: score / total for emotion, score in scores.items()}
    return normalized_scores

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    exit()

prev_time = 0
interval = 3

emotion_score = {"happy": 0, "sad": 0, "neutral": 0, "angry": 0, "fear": 0, "surprise": 0}

with mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as face_mesh:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)
        mask = np.zeros_like(frame, dtype=np.uint8)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                h, w, _ = frame.shape
                landmarks = np.array(
                    [[int(pt.x * w), int(pt.y * h)] for pt in face_landmarks.landmark]
                )

                mouth_indices = [61, 291, 0, 17, 78, 308, 13, 14, 87, 317]
                mask_points = landmarks[mouth_indices]
                cv2.fillPoly(mask, [mask_points], (255, 255, 255))
                masked_frame = cv2.addWeighted(frame, 0.7, mask, 0.3, 0)

                mp_drawing.draw_landmarks(
                    image=masked_frame,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style(),
                )

                current_time = time.time()
                if current_time - prev_time > interval:
                    prev_time = current_time
                    emotion_score = analyze_emotion(face_landmarks)
        else:
            masked_frame = frame.copy()

        emotion_text = ", ".join([f"{emotion}: {score:.2f}" for emotion, score in emotion_score.items()])
        cv2.putText(masked_frame, emotion_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Live Masked Emotion Detection", masked_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
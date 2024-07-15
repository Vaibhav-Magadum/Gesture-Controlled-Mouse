import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize video capture and MediaPipe Hands
cap = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

# Variables to keep track of gesture states
gesture_start_time = time.time()
prev_x, prev_y = 0, 0
gesture_threshold = 40  # Adjust this threshold based on your setup

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)  # Flip the frame horizontally
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert the BGR frame to RGB
    results = hands.process(rgb_frame)  # Process the frame and find hands
    multi_hand_landmarks = results.multi_hand_landmarks
    
    if multi_hand_landmarks:  # Check if any hand landmarks are detected
        for hand_landmarks in multi_hand_landmarks:
            drawing_utils.draw_landmarks(frame, hand_landmarks)  # Draw landmarks on the frame
            
            # Extract index finger tip and thumb tip landmarks
            index_finger_tip = hand_landmarks.landmark[8]
            thumb_tip = hand_landmarks.landmark[4]
            
            # Convert landmarks to frame coordinates
            index_x = int(index_finger_tip.x * frame_width)
            index_y = int(index_finger_tip.y * frame_height)
            thumb_x = int(thumb_tip.x * frame_width)
            thumb_y = int(thumb_tip.y * frame_height)
            
            # Draw circles on the index finger and thumb tips
            cv2.circle(frame, (index_x, index_y), 10, (0, 255, 255), -1)
            cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 255, 255), -1)
            
            # Detect swipe gestures
            if prev_x != 0 and prev_y != 0:
                diff_x = index_x - prev_x
                diff_y = index_y - prev_y
                if abs(diff_x) > abs(diff_y):
                    if diff_x > gesture_threshold:
                        # Swipe right: Next slide
                        pyautogui.press('right')
                        gesture_start_time = time.time()
                    elif diff_x < -gesture_threshold:
                        # Swipe left: Previous slide
                        pyautogui.press('left')
                        gesture_start_time = time.time()
                prev_x, prev_y = index_x, index_y

            # Check for pinch gesture to start/end presentation
            if abs(index_x - thumb_x) < 20 and abs(index_y - thumb_y) < 20:
                if time.time() - gesture_start_time > 2:
                    pyautogui.press('f5')  # Start or end presentation
                    gesture_start_time = time.time()
            else:
                prev_x, prev_y = index_x, index_y
    
    cv2.imshow('frame', frame)  # Display the frame
    if cv2.waitKey(1) & 0xFF == 27:  # Exit on 'Esc' key press
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

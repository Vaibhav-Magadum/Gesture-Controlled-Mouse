import cv2
import mediapipe as mp
import pyautogui

# Initialize video capture and MediaPipe Hands
cap = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0

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
            
            # Extract index finger and thumb landmarks
            index_finger_tip = hand_landmarks.landmark[8]
            thumb_tip = hand_landmarks.landmark[4]
            
            # Convert landmarks to screen coordinates
            index_x = int(index_finger_tip.x * frame_width)
            index_y = int(index_finger_tip.y * frame_height)
            screen_index_x = screen_width / frame_width * index_x
            screen_index_y = screen_height / frame_height * index_y
            
            thumb_x = int(thumb_tip.x * frame_width)
            thumb_y = int(thumb_tip.y * frame_height)
            
            # Move the mouse cursor
            pyautogui.moveTo(screen_index_x, screen_index_y)
            
            # Draw circles on the index finger and thumb tips
            cv2.circle(frame, (index_x, index_y), 10, (0, 255, 255), -1)
            cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 255, 255), -1)
            
            # Check the distance between index finger and thumb
            if abs(index_y - thumb_y) < 20:
                pyautogui.click()
    
    cv2.imshow('frame', frame)  # Display the frame
    if cv2.waitKey(1) & 0xFF == 27:  # Exit on 'Esc' key press
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

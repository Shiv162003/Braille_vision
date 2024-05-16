import cv2
import os
from matplotlib import pyplot as plt
import mediapipe as mp
from gtts import gTTS
from IPython.display import Audio, display
import numpy as np
from tensorflow.keras.models import load_model
import streamlit as st
from io import BytesIO
def is_connection_successful(url):
    # Initialize webcam
    cap = cv2.VideoCapture(url)
    
    # Check if the connection is successful
    if cap.isOpened():
        cap.release()
        return True
    else:
        return False

def capture_and_save_image(url, save_directory):
    # Initialize webcam
    cap = cv2.VideoCapture(url)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    # Capture image
    ret, frame = cap.read()
    
    if ret:
        # Rotate the captured frame by 180 degrees
        rotated_frame = cv2.flip(frame, -1)  # Flip both horizontally and vertically
        
        # Create directory to save images if it doesn't exist
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        
        # Save rotated image
        image_path = os.path.join(save_directory, "img1.jpg")
        cv2.imwrite(image_path, rotated_frame)
        print("Image captured, rotated 180 degrees, and saved.")
        
    else:
        print("Error capturing image.")
    
    # Release webcam
    cap.release()


def crop_image_from_all_sides(input_image_path, output_image_path):
    # Read the input image using OpenCV
    img = cv2.imread(input_image_path)
    top= 0
    bottom = 550
    left = 790
    right = 30
    # Get the dimensions of the input image
    height, width = img.shape[:2]
    
    # Calculate the cropping dimensions
    top_crop = min(top, height)
    bottom_crop = min(bottom, height - top_crop)
    left_crop = min(left, width)
    right_crop = min(right, width - left_crop)
    
    # Crop the image
    cropped_img = img[top_crop:(height - bottom_crop), left_crop:(width - right_crop)]
    
    # Save the cropped image
    cv2.imwrite(output_image_path, cropped_img)



def extract_sub_images(input_image_path):
    # Load the image
    num_rows=3
    num_cols=10
    image = cv2.imread(input_image_path)
    
    # Calculate the height and width of the image
    height, width, _ = image.shape
    height, width, _ = image.shape

    # Define custom row heights (adjust as needed)
    row_heights = [height // 4, height // 4, height // 4, height // 4]
    
    # Create a list to store individual boxes
    boxes = []

    for i in range(num_rows):
        y1 = sum(row_heights[:i])
        y2 = sum(row_heights[:i + 1])

        for j in range(num_cols):
            x1 = j * (width // num_cols)
            x2 = (j + 1) * (width // num_cols)

            box = image[y1:y2, x1:x2]
            boxes.append(box)

    return boxes


def detect_and_save_index_finger(image_path, output_image_path):
    # Load image
    image = cv2.imread(image_path)

    # Initialize MediaPipe hands module
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2)

    # Convert the BGR image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image with MediaPipe hands
    results = hands.process(image_rgb)

    # Draw index finger landmark on the image
    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]  # Assuming only one hand is detected
        index_finger_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        height, width, _ = image.shape
        x, y = int(index_finger_landmark.x * width), int(index_finger_landmark.y * height)
        cv2.circle(image, (x, y), 15, (0, 255, 0), -1)  # Increase the radius to 10 pixels

    # Save the image with detected index finger
    cv2.imwrite(output_image_path, image)

    # Release resources
    hands.close()


def text_to_speech(text, language='en'):
    # Initialize the gTTS object with the text and language
    tts = gTTS(text=text, lang=language, slow=False)
    
    # Save the speech as a temporary audio file
    audio_stream = BytesIO()
    tts.write_to_fp(audio_stream)
    
    # Play the speech using Streamlit's audio widget
    st.audio(audio_stream.getvalue(), format='audio/mp3')

def classify_image(image_path):

    model = load_model("braille_model.h5")

    # Preprocess the image
    if not os.path.isfile(image_path):
        raise ValueError("Invalid image file path. File does not exist.")
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError("Invalid image file format.")
    img = cv2.resize(img, (32, 32)) / 255.0  # Resize and normalize
    img = img.reshape(-1, 32, 32, 1)

    # Perform classification
    predictions = model.predict(img)

    # Get the predicted class
    predicted_class = chr(ord('a') + np.argmax(predictions))

    return predicted_class



def detect_green_dot(image_path):
    # Read the image
    image = image_path
    
    # Convert the image to HSV (Hue, Saturation, Value) color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define range of green color in HSV
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])
    
    # Threshold the HSV image to get only green colors
    mask = cv2.inRange(hsv_image, lower_green, upper_green)
    
    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Check if any contours are found
    if contours:
        # Loop through all contours
        for contour in contours:
            # Calculate area of contour
            area = cv2.contourArea(contour)
            
            # If the area is large enough, consider it as a green dot
            if area > 10:
                return True  # Green dot found
    
    return False  # No green dot found


import streamlit as st
import cv2
import os
import time
from matplotlib import pyplot as plt
import mediapipe as mp
from gtts import gTTS
from IPython.display import Audio, display
import numpy as np
from tensorflow.keras.models import load_model
from io import BytesIO
from streamlit_option_menu import option_menu
l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from functions import is_connection_successful, capture_and_save_image, crop_image_from_all_sides, extract_sub_images , detect_and_save_index_finger,classify_image, detect_green_dot


import speech_recognition as sr


def audio_to_text(audio_data):
    recognizer = sr.Recognizer()
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Unable to recognize speech"
    except sr.RequestError as e:
        return f"Error: {e}"



def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='en')  # Generate text to speech
    tts.save(filename)  # Save the speech as a file

def page2():
    selected =option_menu(menu_title=None,options=["Learn Braille","Line-Practice"],orientation="horizontal",)
    if selected=="Learn Braille":
        c=0
        st.title("Lets Set up the Camera ")
        url = st.text_input("Enter the URL of the webcam:")
        if st.button("Check Connection"):
            if is_connection_successful(url):
                st.success("Connection Successful!")
                save_directory = "withouthand"
                with st.spinner("Capturing image..."):
                    capture_and_save_image(url, save_directory)
                    
                st.success("Image Captured successfully!")
    
                
                image_path = "withouthand/img1.jpg"
                output_image_path = "withouthand/cropped_image.jpg"  # Change this to the desired output path
                with st.spinner("Cropping image..."):
                    crop_image_from_all_sides(image_path, output_image_path)
                    
                st.success("Image cropped successfully!")
    
                with st.spinner("Segmenting Image"):
                    x=extract_sub_images("withouthand/cropped_image.jpg")
                    
                st.success("Image segmented successfully!")
    
                
            else:
                st.error("Connection Failed!")




        
    
        mm=0
        text1="hello"
        counter=0
        if st.button("Let's start"):
            while True:
                mm=mm+1
                save_directory = "withhand"
                capture_and_save_image(url, save_directory)
                detect_and_save_index_finger("withhand/img1.jpg","withhand/x.jpg")
                image_path = "withhand/x.jpg"
                output_image_path = "withhand/cropped_image.jpg"  # Change this to the desired output path
                crop_image_from_all_sides(image_path, output_image_path)
                y = extract_sub_images("withhand/cropped_image.jpg")
                m = -1
                
                for i in range(0,30):
                    if detect_green_dot(y[i]):
                        m = i
                        break
                if m == -1:
                    text = "Please put your finger on a set of six dots"
                else:
                    text = l[m]
                    print(text)
                if text1!=text :    
                    filename = "hello_world"+str(mm)+".mp3"
                    text_to_speech(text, filename)
                    st.audio(filename, format='audio/mp3')
                    os.system("start " + filename)
                    text1=text
                time.sleep(3)




    
    if selected=="Line-Practice":
         url = st.text_input("Enter the URL of the webcam:")
         mm=0
         text1="hello"
         text2=""
         counter=0
         x=0
         if st.button("Let's start"):
                mm=mm+1
                save_directory = "withhand"
                capture_and_save_image(url, save_directory)
                detect_and_save_index_finger("withhand/img1.jpg","withhand/x.jpg")
                image_path = "withhand/x.jpg"
                output_image_path = "withhand/cropped_image.jpg"  # Change this to the desired output path
                crop_image_from_all_sides(image_path, output_image_path)
                y = extract_sub_images("withhand/cropped_image.jpg")
                m = -1 
                for i in range(0,30):
                    if detect_green_dot(y[i]):
                        m = i
                        break
                if m == -1:
                    text = "Please put your finger on a set of six dots"
                else:
                    text = l[m]
                    text2=l[m+1]
                        
                filename = "hello_world"+str(mm)+".mp3"
                text_to_speech(text, filename)
                st.audio(filename, format='audio/mp3')
                os.system("start " + filename)             
                time.sleep(3)
                while x==0:
                    mm=mm+1
                    save_directory = "withhand"
                    capture_and_save_image(url, save_directory)
                    detect_and_save_index_finger("withhand/img1.jpg","withhand/x.jpg")
                    image_path = "withhand/x.jpg"
                    output_image_path = "withhand/cropped_image.jpg"  # Change this to the desired output path
                    crop_image_from_all_sides(image_path, output_image_path)
                    y = extract_sub_images("withhand/cropped_image.jpg")
                    m = -1 
                    for i in range(0,30):
                        if detect_green_dot(y[i]):
                            m = i
                            break
                    if m == -1:
                        text = "Finger not detected"
                    else:
                        text = l[m]
                    if(text2==text):
                        text2=l[m+1]
                        filename = "hello_world"+str(mm)+".mp3"
                        text_to_speech(text, filename)
                        st.audio(filename, format='audio/mp3')
                        os.system("start " + filename)             
                        time.sleep(3)
                    else:
                        text = "You are off the line please restart"
                        filename = "hello_world"+str(mm)+".mp3"
                        text_to_speech(text, filename)
                        st.audio(filename, format='audio/mp3')
                        os.system("start " + filename)             
                        time.sleep(3)
                        x=x+1
            





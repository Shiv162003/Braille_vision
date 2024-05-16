import streamlit as st
from module import page2
from PIL import Image
import os
from streamlit_option_menu import option_menu
def main():
    st.set_page_config(page_title="Braille Vision", page_icon=Image.open("assets/logo.jpeg"), layout="wide")   
    if st.session_state.page == "About":
        col1, col2, col3,col4,col5 = st.columns([1, 1, 1,1,1])  # Create columns to adjust centering
        with col3:
            st.image('assets/image 1.jpeg', width=300, use_column_width=False)  # Adjust the width as needed        
        
        selected =option_menu(menu_title=None,options=["Home","About Us"],orientation="horizontal",)  
        
        if selected=="Home":
            st.markdown("""<h1 style='text-align: center;'>Welcome To Braille_Vision</h1>""", unsafe_allow_html=True)
            col1, col2= st.columns([1, 1])
            with col1:
                st.header("What is Braille?")
                st.markdown("""
                Braille is a tactile writing system that allows blind and visually impaired people to read and write through touch. It was invented by Louis Braille in the early 19th century. The system is based on a series of raised dots arranged in patterns within cells. Each cell can contain up to six dots, arranged in two columns of three dots each. By feeling the dots with their fingertips, users can interpret the characters represented by the dot patterns.
                """)
                st.header("How Does Braille Work?")
                st.markdown("""
               Braille is crucial for literacy and independence among blind and visually impaired individuals. It provides access to information and enables communication in various contexts, including education, employment, and daily life. Learning Braille empowers individuals to read books, write notes, access information on signs and labels, and communicate effectively with others.
                """)
    
                st.header("Importance of Braille")
                st.markdown("""
               Braille characters represent letters, numbers, punctuation marks, and even musical and mathematical symbols. Each character or symbol is formed by a unique combination of dots within a cell. For example, the letter "A" is represented by a single dot in the top-left corner of the cell, while the letter "B" is represented by dots in the top-left and middle-left positions.
                """)
            with col2:
                st.image('assets/image 2.jpg', width=900, use_column_width=False)
           
            
            
            
            st.markdown("""<h1 style='text-align: center;'>What is Braille_Vision</h1>""", unsafe_allow_html=True)
            col1, col2= st.columns([1, 1]) 
            with col2:
                st.header("Braille Vision Project")
                st.markdown("""
                **Braille Vision** is a revolutionary project designed to assist individuals in the initial phases of learning Braille. Through innovative image processing and deep learning algorithms, we have developed a compact application capable of recognizing and interpreting tactile inputs. This means that a blind individual can simply place their fingers on a surface, and Braille Vision will accurately identify the Braille characters they are touching.
                Our project provides interactive and audio-guided learning experiences, helping users to familiarize themselves 
                with Braille characters, words, and phrases. With Braille Vision, users can practice their Braille skills 
                anytime and anywhere, making learning more accessible and convenient.
                """)
            
                st.header("How Braille Vision Works")
                st.markdown("""
                1. **Interactive Learning**: Users can interact with a virtual Braille interface, where they can explore 
                   Braille characters and practice forming words and sentences.
                2. **Audio Guidance**: Our application provides audio instructions and feedback to guide users through the 
                   learning process, ensuring a comprehensive learning experience.
                3. **Progress Tracking**: Users can track their learning progress and set personal goals to keep themselves 
                   motivated and engaged.
                """)
            
                st.header("Get Involved")
                st.markdown("""
                We are continuously improving the Braille Vision project to make it more effective and accessible. 
                If you're interested in contributing to our project or providing feedback, please check out our 
                [GitHub repository](https://github.com/Shiv162003/Braille_vision).
                """)
    
                st.header("Know more About Braille and our Project")
                pdf_path = os.path.join("assets", "x.pdf")
                if st.button("Download PDF"):
                    with open(pdf_path, "rb") as file:
                        data = file.read()
                    st.download_button(
                        label="Click here to download the PDF",
                        data=data,
                        file_name="x.pdf",
                        mime="application/pdf"
                    )

            with col1:
                st.image('assets/image 3.jpeg', width=800, use_column_width=False) 

            
            if st.button("Test Braille Vision"):
                st.session_state.page = "Page 2"




        
        if selected=="About Us":
            st.markdown("""<h1 style='text-align: center;'>Meet the Team</h1>""", unsafe_allow_html=True)
            col1, col2, col3,col4,col5 = st.columns([1, 1, 1,1,1]) 
            with col3:
                st.image('assets/group photo.jpg', width=300, use_column_width=False)  # Adjust the width as needed

            col1, col2, col3= st.columns([1, 1, 1])
            with col1:
                st.header(" **Shivansh Nautiyal**")
               
            with col2:
                st.header(" **Riya Aggarwal**")
               
            with col3:
                st.header(" **Shantanu Rokde**")
                
        
            st.header("About Us")
            st.markdown("""
            We are students from Symbiosis Institute of Technology, passionate about solving the problems at hand. 
            As a team, we believe in leveraging technology to address real-world challenges and make a positive 
            impact in our community. With diverse backgrounds and skill sets, we collaborate to innovate and 
            develop solutions that drive meaningful change. Our goal is to create a better, more inclusive world 
            through our work and dedication.
            """)
    
    elif st.session_state.page == "Page 2":
        page2()

if __name__ == "__main__":
    if "page" not in st.session_state:
        st.session_state.page = "About"
    main()

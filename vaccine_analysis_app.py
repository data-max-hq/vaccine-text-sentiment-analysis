import streamlit as st
from openai import OpenAI
import json
import os
import pandas as pd


api_key = os.getenv("OPENAI_API_KEY")


client = OpenAI(
    api_key=api_key  
)


def analyze_data(txt):
    
    st.session_state.analysis_status = "analyzing"
    with placeholder:
        st.info("Analyzing...", icon="🔍")   
        content = f'''
                For the following vaccine related text, return a json object with the following schema: {{
                    "Sentiment": "Pro-Vaccine" | "Negative" | "Anti-Vaccine", 
                    "Intensity": number from 1 to 10, 
                    "Location": any location mentioned in the text, 
                    "Type_of_vaccine": any type of vaccine mentioned in the text
                }}. If you cant find information about one of the fields complete it as unknown. The text is: {txt}
                '''


        # OpenAI API call
        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                f"content":  content,
            }
        ],
        model="gpt-4o",
        temperature=0.1,
        response_format={ "type": "json_object" }
        )
        st.session_state.analysis_status = "analyzed"
        return chat_completion.choices[0].message.content
    

# Initialize session state for button click

st.set_page_config(page_title="Vaccine Text Sentiment Analysis", page_icon="images/ishp_logo.png")

if "analysis_status" not in st.session_state or st.session_state.analysis_status == "analyzed":
    st.session_state.analysis_status = "idle"

st.image("images/cords_logo.jpg")
with st.container(border=True):


    row = st.columns([0.83, 0.17], vertical_alignment="center", border=False)

    with row[0]:    
        with st.container():
            st.markdown("<p style='font-size:36px; font-family:Arial; color:white;'>   Vaccine Text Sentiment Analysis</p>", unsafe_allow_html=True)

    with row[1]:
        with st.container():
            st.image("images/secid_logo.jpg", use_container_width=True)
    


    st.write("This is an app to analyze the sentiment of a post regarding vaccines.")

    txt = st.text_area("Enter a post about vaccines:", height=200)

    placeholder = st.empty()
    if st.button("Analyze"):

        # Reset the analysis status and placeholder on button click
        st.session_state.analysis_status = "idle"
        placeholder.empty()  # Clear placeholder
        response = json.loads(analyze_data(txt))
                              

        
        with st.container(border=True):
            st.metric(label="Sentiment", value=response["Sentiment"])
            st.metric(label="Intensity", value=response["Intensity"])
            st.metric(label="Location", value=response["Location"])
            st.metric(label="Type of Vaccine", value=response["Type_of_vaccine"])


    # Display the final status
    if st.session_state.analysis_status == "analyzed":

        placeholder.success("Analyzed!", icon="✅")


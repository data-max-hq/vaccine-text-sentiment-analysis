import streamlit as st
import json
import os
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("tabularisai/multilingual-sentiment-analysis")
model = AutoModelForSequenceClassification.from_pretrained("tabularisai/multilingual-sentiment-analysis")


def predict_sentiment(text):

    st.session_state.analysis_status = "analyzing"
    with placeholder:
        st.info("Analyzing...", icon="🔍")   
      
        texts = [text]
        inputs = tokenizer(texts, return_tensors="pt", truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
        sentiment_map = {0: "Very Negative", 1: "Negative", 2: "Neutral", 3: "Positive", 4: "Very Positive"}
        st.session_state.analysis_status = "analyzed"

        return [sentiment_map[p] for p in torch.argmax(probabilities, dim=-1).tolist()]


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
        response = predict_sentiment(txt)
                              

        
        with st.container(border=True):
            st.write(response[0])


    # Display the final status
    if st.session_state.analysis_status == "analyzed":

        placeholder.success("Analyzed!", icon="✅")


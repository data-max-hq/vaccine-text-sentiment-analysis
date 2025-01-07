# Vaccine Text Sentiment Analysis
This repo contains code on running a streamlit app that analyzes posts regarding vaccines and return the following result about the text:
```json
{
    "Sentiment": "Pro-Vaccine" | "Negative" | "Anti-Vaccine", 
"Intensity": number from 1 to 10, 
"Location": any location mentioned in the text, 
"Type_of_vaccine": any type of vaccine mentioned in the text
}
```
To run the application create an .env file and insert the following variable with a proper open ai api token:
```
OPENAI_API_TOKEN=
```
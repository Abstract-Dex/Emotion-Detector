import streamlit as st
from transformers import pipeline

st.title('Emotion :blue[Detector]')

st.write('This is a simple web app to predict the emotion of a given user input.')

# User input box
user_input = st.text_area('Enter your text here:')

if st.button('Predict'):
    pipe = pipeline("text-classification",
                    model="Foulbubble/Emotion-Detector")
    pred = pipe(user_input)
    id2label = {"LABEL_0": "sadness", "LABEL_1": "joy", "LABEL_2": "love",
                "LABEL_3": "anger", "LABEL_4": "fear", "LABEL_5": "surprise"}
    # map the label to the emotion
    pred[0]["label"] = id2label[pred[0]["label"]]
    st.write(f'The predicted emotion is: {pred[0]["label"]}')

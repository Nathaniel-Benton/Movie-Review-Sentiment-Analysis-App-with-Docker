# Load libraries
import streamlit as st
import pandas as pd
import joblib

# 1. Title
st.title("Movie Review Sentiment Analyzer")

# 2. App Description
st.write("This app recieves an input of a movie review, and determines the likely sentiment of the reviewer")

# --- Caching the model ---
# Use st.cache_data to load the model only once
@st.cache_data
def load_model():
    """Loads the pre-trained model."""
    model = joblib.load("sentiment_model.pkl")
    return model

# Load the model
model = load_model()

# Movie review for user input
user_text = st.text_area("Enter a movie review to analyze:")

# If statement for button operations
if st.button("Analyze"):
    if user_text.strip() == "":
        st.warning("Please enter a movie review above and press the Analyze button again.")

    else:
        sentiment_prediction = model.predict([user_text])[0]
        sentiment_probability = model.predict_proba([user_text])[0]

        if sentiment_prediction == "positive":
            st.success("Predicted Sentiment: Positive 👍")
            confidence = sentiment_probability[1] * 100

        else:
            st.error("Predicted Sentiment: Negative 👎")
            confidence = sentiment_probability[0] * 100

        st.write(f"Confidence of Prediction: {confidence:.2f}%")



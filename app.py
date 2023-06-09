import streamlit as st
from textblob import TextBlob
import matplotlib.pyplot as plt

# Function for analyzing sentiment using TextBlob
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_polarity = blob.sentiment.polarity
    sentiment_subjectivity = blob.sentiment.subjectivity
    return sentiment_polarity, sentiment_subjectivity

# Function for displaying a visual representation of the sentiment analysis results
def display_sentiment_analysis(polarity, subjectivity):
    fig, ax = plt.subplots()
    ax.bar(["Polarity", "Subjectivity"], [polarity, subjectivity])
    ax.set_ylim([-1, 1])
    ax.set_ylabel("Value")
    ax.set_title("Sentiment Analysis Results")
    st.pyplot(fig)

# Main function for running the streamlit app
def main():
    st.title("Sentiment Analysis with TextBlob")
    st.write("Enter a piece of text to analyze its sentiment.")
    text = st.text_input("Text Input")
    
    if st.button("Analyze"):
        if text:
            try:
                polarity, subjectivity = analyze_sentiment(text)
                st.write(f"Polarity: {polarity}")
                st.write(f"Subjectivity: {subjectivity}")
                display_sentiment_analysis(polarity, subjectivity)
            except:
                st.write("An error occurred while analyzing the sentiment.")
        else:
            st.write("Please enter a piece of text to analyze.")

if __name__ == "__main__":
    main()

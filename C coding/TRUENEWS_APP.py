import streamlit as st
import pandas as pd
import re
import nltk
import numpy as np
import openai
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

@st.cache_resource
def load_model():
    df = pd.read_csv("liar_dataset/train.tsv", sep='\t', header=None)
    df.columns = ["label", "statement", "subject", "speaker", "speaker_job", "state", "party",
                  "barely_true_counts", "false_counts", "half_true_counts", "mostly_true_counts",
                  "pants_on_fire_counts", "context"]

    def clean_text(text):
        text = str(text).lower()
        text = re.sub(r'[^\w\s]', '', text)
        return ' '.join(word for word in text.split() if word not in stop_words)

    df['clean_statement'] = df['statement'].apply(clean_text)

    def label_group(label):
        return 'fake' if label in ['false', 'pants-fire', 'barely-true'] else 'real'

    df['binary_label'] = df['label'].apply(label_group)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['clean_statement'])
    y = df['binary_label']
    model = MultinomialNB().fit(X, y)

    return model, vectorizer

model, vectorizer = load_model()

st.title("📰 Fake News Detector")

option = st.selectbox("Choose mode:", ("Local Model (Offline)", "OpenAI GPT Model (Online)"))
text = st.text_area("Enter news statement:")

if option == "OpenAI GPT Model (Online)":
    api_key = st.text_input("Enter your OpenAI API key:", type="password")

if st.button("Predict"):
    if option == "Local Model (Offline)":
        cleaned = ' '.join(word for word in re.sub(r'[^\w\s]', '', text.lower()).split() if word not in stop_words)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]
        st.success(f"Prediction: **{prediction.upper()}** (Local Model)")
    
    elif option == "OpenAI GPT Model (Online)" and api_key:
        try:
            openai.api_key = api_key
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Classify the following news as real or fake. Only reply with 'REAL' or 'FAKE'."},
                    {"role": "user", "content": text}
                ]
            )
            result = response['choices'][0]['message']['content'].strip()
            st.success(f"Prediction: **{result.upper()}** (GPT Model)")
        except Exception as e:
            st.error(f"Error with OpenAI API: {e}")

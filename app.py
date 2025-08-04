import streamlit as st
import pickle 
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

# Initialize
ps = PorterStemmer()

# Function to transform text
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load model and vectorizer
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# --- Webpage Styling ---
st.set_page_config(page_title="Spam Detector", page_icon="📩", layout="centered")

st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>📩 Email/SMS Spam Classifier</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; font-size: 18px;'>Enter a message below and click <b>Predict</b> to check if it's <span style='color:red;'>Spam</span> or <span style='color:green;'>Not Spam</span>.</p>",
    unsafe_allow_html=True
)

# Input Area
with st.container():
    input_sms = st.text_area('✍️ Type your message here:')

# Predict Button
if st.button('🚀 Predict'):
    if input_sms.strip() == "":
        st.warning("Please enter a message first.")
    else:
        # Preprocess
        transformed_text = transform_text(input_sms)
        # Vectorize
        vector_input = tfidf.transform([transformed_text])
        # Predict
        result = model.predict(vector_input)[0]

        # Display Result
        if result == 1:
            st.error("🔴 This message is **SPAM**.")
        else:
            st.success("🟢 This message is **NOT SPAM**.")
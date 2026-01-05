import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_models():
    sent_pipe = pipeline("sentiment-analysis")
    sum_pipe = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    return sent_pipe, sum_pipe

st.title("Review X-Ray")
st.write("Paste a product review to get the vibe and the summary.")

text = st.text_area("Customer Review", height=200)

if st.button("Analyze"):
    if text:
        with st.spinner("Analyzing..."):
            sent_model, sum_model = load_models()
            sentiment = sent_model(text)[0]
            summary = sum_model(text, max_length=100, min_length=10, do_sample=False)[0]
         
            col1, col2 = st.columns(2) #display res
            
            with col1:
                st.subheader("Sentiment")
                label = sentiment['label']
                score = round(sentiment['score'] * 100, 2)
                if label == "POSITIVE":
                    st.success(f"{label} ({score}%)")
                else:
                    st.error(f"{label} ({score}%)")
            
            with col2:
                st.subheader("TL;DR Summary")
                st.info(summary['summary_text'])
    else:
        st.warning("Please paste some text first!")
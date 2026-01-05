Review X-Ray is an NLP (Natural Language Processing) application designed to automate the analysis of unstructured customer feedback. 

In high-volume e-commerce environments, reading every review is impossible. This tool solves that problem by using two distinct Deep Learning models to:
1. Detect Sentiment: Instantly classify feedback as Positive or Negative.
2. Generate Summaries: Condense long, rambling reviews into concise "TL;DR" insights.

Features
* Multi-Model Pipeline: DistilBERT for sentiment analysis and BART for abstractive summarization.
* Real-Time Inference: Processes text inputs instantly via a lightweight web interface.
* Optimized Performance: Uses caching decorators to minimize model reload times.

Tech Stack
* Language: Python
* ML Libraries: Hugging Face Transformers, PyTorch
* Web Framework: Streamlit

Virtual Environment
.venv/
venv/

Usage
Run the application locally:
bash: streamlit run main.py

import streamlit as st
import fitz  # PyMuPDF
import plotly.graph_objects as go
from collections import Counter
import numpy as np

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to generate 3D word cloud
def generate_3d_wordcloud(text):
    word_counts = Counter(text.split())
    words = list(word_counts.keys())
    counts = list(word_counts.values())
    
    # Generate random positions for words
    np.random.seed(42)
    x = np.random.randn(len(words))
    y = np.random.randn(len(words))
    z = np.random.randn(len(words))
    
    # Create a 3D scatter plot
    fig = go.Figure(data=[go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='text',
        text=words,
        marker=dict(
            size=np.log(np.array(counts) + 1) * 10,
            color=counts,
            colorscale='Viridis',
            opacity=0.8
        ),
        textfont=dict(size=np.log(np.array(counts) + 1) * 10, color='white')
    )])
    
    fig.update_layout(scene=dict(aspectmode='cube'), showlegend=False)
    return fig

# Streamlit app
st.title("PDF to 3D Word Cloud Generator")

# Upload PDF file
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_file is not None:
    # Extract text from PDF
    text = extract_text_from_pdf(uploaded_file)

    # Generate 3D word cloud
    fig = generate_3d_wordcloud(text)
    st.plotly_chart(fig)

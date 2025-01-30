import streamlit as st
import fitz  # PyMuPDF
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to generate word cloud image
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig("wordcloud.png", format="png")
    return "wordcloud.png"

# Streamlit app
st.title("PDF to Word Cloud Generator")

# Upload PDF file
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_file is not None:
    # Extract text from PDF
    text = extract_text_from_pdf(uploaded_file)
    st.write("Extracted Text:")
    st.write(text)

    # Generate word cloud
    wordcloud_image = generate_wordcloud(text)
    st.image(wordcloud_image, use_column_width=True)

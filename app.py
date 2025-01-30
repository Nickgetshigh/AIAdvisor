import streamlit as st
import fitz  # PyMuPDF
import plotly.graph_objects as go
import imageio
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to create 3D word positions
def generate_3d_word_positions(words, size=30):
    np.random.seed(42)
    positions = np.random.rand(len(words), 3)
    return positions

# Function to generate frames for 3D word cloud
def generate_3d_wordcloud_frames(words, positions, num_frames=30):
    frames = []
    for i in range(num_frames):
        fig = go.Figure(data=[go.Scatter3d(
            x=positions[:,0],
            y=positions[:,1],
            z=positions[:,2],
            mode='text',
            text=words,
            textfont=dict(size=12, color='black')
        )])
        fig.update_layout(scene=dict(aspectmode='cube'), showlegend=False)
        image_path = f"frame_{i}.png"
        fig.write_image(image_path)
        frames.append(imageio.imread(image_path))
        os.remove(image_path)
    return frames

# Streamlit app
st.title("PDF to 3D Word Cloud GIF Generator")

# Upload PDF file
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_file is not None:
    # Extract text from PDF
    text = extract_text_from_pdf(uploaded_file)
    st.write("Extracted Text:")
    st.write(text)
    
    words = text.split()
    positions = generate_3d_word_positions(words)
    frames = generate_3d_wordcloud_frames(words, positions)

    # Create GIF
    gif_path = "3d_wordcloud.gif"
    imageio.mimsave(gif_path, frames, fps=2)
    st.image(gif_path)

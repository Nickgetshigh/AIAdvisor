import streamlit as st
from streamlit_lottie import st_lottie
import requests
from gtts import gTTS
import base64
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="For My Girl", page_icon="💖", layout="centered")

# --- CSS FOR THEME ---
st.markdown("""
    <style>
    .stApp {
        background-color: #fceef5;
    }
    h1 {
        color: #d63384;
        text-align: center;
        font-family: 'Dancing Script', cursive;
        font-size: 3rem !important;
    }
    .stButton>button {
        background-color: #d63384;
        color: white;
        border-radius: 30px;
        border: none;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOADING ASSETS ---
def get_lottie(url):
    try:
        r = requests.get(url, timeout=5)
        return r.json() if r.status_code == 200 else None
    except:
        return None

# Soft romantic heart animation
lottie_hearts = get_lottie("https://lottie.host/8040409a-6756-4299-9759-33b68051a029/9f7l8fX7y9.json")

# --- AUDIO FUNCTION ---
def play_audio(text, lang):
    try:
        # 'slow=True' makes the voice sound a bit more deliberate/soft
        tts = gTTS(text=text, lang=lang, slow=True)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        audio_b64 = base64.b64encode(fp.read()).decode()
        audio_tag = f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_b64}">'
        st.markdown(audio_tag, unsafe_allow_html=True)
    except:
        pass

# --- SESSION STATE ---
if 'language' not in st.session_state:
    st.session_state.language = 'Chinese'

# --- DISPLAY ---
if lottie_hearts:
    st_lottie(lottie_hearts, height=300, key="romance")

# Question Logic
if st.session_state.language == 'Chinese':
    # "Babe, do you want to bite me?" in Chinese
    main_text = "宝贝，你想咬我吗？" 
    lang_code = 'zh-cn'
    btn_label = "Translate to Hindi 🇮🇳"
else:
    # "Babe, do you want to bite me?" in Hindi
    main_text = "बेबी, क्या तुम मुझे काटना चाहती हो?" 
    lang_code = 'hi'
    btn_label = "Translate to Chinese 🇨🇳"

# Display the question
st.markdown(f"<h1>{main_text}</h1>", unsafe_allow_html=True)

# Audio Autoplay
play_audio(main_text, lang_code)

# Language Toggle
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button(btn_label):
        st.session_state.language = 'Hindi' if st.session_state.language == 'Chinese' else 'Chinese'
        st.rerun()

st.write("---")

# Buttons
c1, c2 = st.columns(2)
with c1:
    if st.button("YES! 🦷❤️", use_container_width=True):
        st.balloons()
        st.markdown("<h2 style='text-align:center;'>Ouch! But I love it. 😘</h2>", unsafe_allow_html=True)
        celebrate = get_lottie("https://lottie.host/67702580-f00a-42fb-a7e8-e4b779a5e8c1/m8n8C0zE9Y.json")
        st_lottie(celebrate, height=200)

with c2:
    if st.button("No 🥺", use_container_width=True):
        st.write("Why not? I'm delicious! 🍫")

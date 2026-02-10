import streamlit as st
from streamlit_lottie import st_lottie
import requests
from gtts import gTTS
import base64
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="For You", page_icon="❤️", layout="centered")

# --- CUSTOM CSS FOR THEME ---
st.markdown("""
    <style>
    .stApp {
        background-color: #fff0f3;
    }
    h1 {
        color: #ff4d6d;
        text-align: center;
        font-family: 'Georgia', serif;
    }
    .stButton>button {
        background-color: #ff4d6d;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 25px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff758f;
        border: 1px solid white;
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

lottie_url = "https://lottie.host/8040409a-6756-4299-9759-33b68051a029/9f7l8fX7y9.json"
lottie_hearts = get_lottie(lottie_url)

# --- AUDIO FUNCTION ---
def play_audio(text, lang):
    try:
        # Added a bit of 'slow' for a softer Hindi delivery
        tts = gTTS(text=text, lang=lang, slow=False)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        audio_b64 = base64.b64encode(fp.read()).decode()
        audio_tag = f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_b64}">'
        st.markdown(audio_tag, unsafe_allow_html=True)
    except Exception as e:
        pass

# --- APP LOGIC ---
if 'language' not in st.session_state:
    st.session_state.language = 'Chinese'

if lottie_hearts:
    st_lottie(lottie_hearts, height=250, key="main_heart")

# Content Management
if st.session_state.language == 'Chinese':
    main_text = "你会跟我做爱吗？" # Chinese for the updated request
    lang_code = 'zh-cn'
    btn_label = "Translate to Hindi 🇮🇳"
else:
    # Hindi for the updated request
    main_text = "क्या तुम मेरे साथ हमबिस्तर होगी?" 
    lang_code = 'hi'
    btn_label = "Translate to Chinese 🇨🇳"

# Display Text
st.markdown(f"<h1>{main_text}</h1>", unsafe_allow_html=True)

# Translation Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button(btn_label, use_container_width=True):
        st.session_state.language = 'Hindi' if st.session_state.language == 'Chinese' else 'Chinese'
        st.rerun()

# Play Audio
play_audio(main_text, lang_code)

st.write("---")
c1, c2 = st.columns(2)

with c1:
    if st.button("YES! 😍", use_container_width=True):
        st.balloons()
        # Celebration animation
        celebrate = get_lottie("https://lottie.host/67702580-f00a-42fb-a7e8-e4b779a5e8c1/m8n8C0zE9Y.json")
        st_lottie(celebrate, height=200)

with c2:
    if st.button("No 😢", use_container_width=True):
        st.warning("Try again! 😉")

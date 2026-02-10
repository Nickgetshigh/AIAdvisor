import streamlit as st
from streamlit_lottie import st_lottie
import requests
from gtts import gTTS
import base64
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="For My Love", page_icon="❤️", layout="centered")

# --- CUSTOM CSS FOR THEME ---
st.markdown("""
    <style>
    .stApp {
        background-color: #fff0f3;
    }
    h1 {
        color: #ff4d6d;
        text-align: center;
    }
    .stButton>button {
        background-color: #ff4d6d;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 25px;
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

# Latest stable Lottie URL
lottie_url = "https://lottie.host/8040409a-6756-4299-9759-33b68051a029/9f7l8fX7y9.json"
lottie_hearts = get_lottie(lottie_url)

# --- AUDIO FUNCTION ---
def play_audio(text, lang):
    try:
        tts = gTTS(text=text, lang=lang)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        audio_b64 = base64.b64encode(fp.read()).decode()
        # Hidden autoplay audio tag
        audio_tag = f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_b64}">'
        st.markdown(audio_tag, unsafe_allow_html=True)
    except Exception as e:
        st.error("Audio could not be generated.")

# --- APP LOGIC ---
if 'language' not in st.session_state:
    st.session_state.language = 'Chinese'

# Display Animation
if lottie_hearts:
    st_lottie(lottie_hearts, height=250, key="main_heart")
else:
    st.title("❤️") # Fallback if URL fails

# Language Content
if st.session_state.language == 'Chinese':
    main_text = "你会做我的情人吗？"
    sub_text = "(Will you be my Valentine?)"
    lang_code = 'zh-cn'
    btn_label = "Translate to Hindi 🇮🇳"
else:
    main_text = "क्या तुम मेरी वैलेंटाइन बनोगी?"
    sub_text = "(Will you be my Valentine?)"
    lang_code = 'hi'
    btn_label = "Translate to Chinese 🇨🇳"

# Display Text
st.markdown(f"<h1>{main_text}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #ff758f;'>{sub_text}</p>", unsafe_allow_html=True)

# Translation Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button(btn_label, use_container_width=True):
        st.session_state.language = 'Hindi' if st.session_state.language == 'Chinese' else 'Chinese'
        st.rerun()

# Play Audio automatically on load/change
play_audio(main_text, lang_code)

# Final Question Buttons
st.write("---")
c1, c2 = st.columns(2)

with c1:
    if st.button("YES! 😍", use_container_width=True):
        st.balloons()
        st.success("Yay! Best Valentine ever! ❤️")
        st.confetti() # Only works on some streamlit versions, st.balloons is safer

with c2:
    # A little joke for the 'No' button
    if st.button("No 😢", use_container_width=True):
        st.warning("Error: This button is broken. Try the other one! 😉")

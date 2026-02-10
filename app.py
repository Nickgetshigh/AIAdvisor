import streamlit as st
from streamlit_lottie import st_lottie
import requests
from gtts import gTTS
import base64
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="For My Bbygirl", page_icon="🔞", layout="centered")

# --- CUSTOM ROMANTIC CSS ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(to bottom, #1a1a2e, #16213e); }
    .stButton>button {
        background-color: #e94560;
        color: white;
        border-radius: 12px;
        height: 3.5em;
        width: 100%;
        border: none;
        font-weight: bold;
        font-size: 16px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff2e63;
        transform: translateY(-2px);
        box-shadow: 0px 4px 15px rgba(233, 69, 96, 0.4);
    }
    .message-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #e94560;
        text-align: center;
        color: #ff2e63;
        font-size: 20px;
        margin-bottom: 20px;
        font-style: italic;
        font-weight: bold;
    }
    hr { border: 0.5px solid #e94560; }
    </style>
    """, unsafe_allow_html=True)

# --- UTILITY FUNCTIONS ---
def get_lottie(url):
    try:
        r = requests.get(url, timeout=3)
        return r.json() if r.status_code == 200 else None
    except: return None

def play_audio(text, lang):
    try:
        # Using 'en-uk' or 'en-au' sometimes triggers a deeper voice profile in gTTS
        tts = gTTS(text=text, lang=lang, slow=False)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        audio_b64 = base64.b64encode(fp.read()).decode()
        audio_tag = f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_b64}">'
        st.markdown(audio_tag, unsafe_allow_html=True)
    except: st.error("Audio Error")

# --- APP LAYOUT ---
lottie_url = "https://lottie.host/8040409a-6756-4299-9759-33b68051a029/9f7l8fX7y9.json"
lottie_main = get_lottie(lottie_url)
if lottie_main:
    st_lottie(lottie_main, height=250, key="main")

st.markdown("<h2 style='text-align: center; color: white;'>Do you want me?</h2>", unsafe_allow_html=True)

# --- RHYTHMIC RHYMING DATA ---
# Note: 'en-uk' is used for a deeper, more formal tone which can sound more masculine
msg_data = {
    "English 🇬🇧": {
        "txt": "So you want me, and you need me... Come and please me, keep it steamy. Up and down, and round and round... I’m the best thing that you’ve found.", 
        "code": "en-uk" 
    },
    "Spanish 🇪🇸": {
        "txt": "Tú me quieres, tú me llamas... Ven ahora a mi cama. De arriba abajo, sin descansar... Te voy a hacer vibrar.", 
        "code": "es"
    },
    "Hindi 🇮🇳": {
        "txt": "Chaho mujhe, ya karo intezaar... Aa jao paas, mitao pyaas. Upar niche, gol gol... Dil ki baatein, ab tu khol.", 
        "code": "hi"
    },
    "French 🇫🇷": {
        "txt": "Tu me veux, tu me tiens... Viens ici, tu es mienne. De haut en bas, tout en rondeur... Je vais conquérir ton cœur.", 
        "code": "fr"
    }
}

# --- BUTTON GRID ---
cols = st.columns(2)
for i, (name, info) in enumerate(msg_data.items()):
    with cols[i % 2]:
        if st.button(name):
            st.markdown(f'<div class="message-box">{info["txt"]}</div>', unsafe_allow_html=True)
            play_audio(info['txt'], info['code'])

st.markdown("<br><hr>", unsafe_allow_html=True)

# --- INTERACTIVE BUTTONS ---
c1, c2 = st.columns(2)
with c1:
    if st.button("YES! 😍"):
        st.balloons()
        st.write("### See you soon, baby! 🔥")

with c2:
    if st.button("No 🥺"):
        st.write("Error: Option 'No' is currently out of service. ❤️")

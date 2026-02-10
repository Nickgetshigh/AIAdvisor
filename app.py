import streamlit as st
from streamlit_lottie import st_lottie
import requests
from gtts import gTTS
import base64
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="For My Girl", page_icon="❤️", layout="centered")

# --- STYLE ---
st.markdown("""
    <style>
    .stApp { background-color: #fff0f3; }
    h1 { color: #ff4d6d; text-align: center; font-family: 'Georgia', serif; font-size: 2.5rem; }
    .stSelectbox label { color: #ff4d6d; font-weight: bold; }
    .stButton>button { background-color: #ff4d6d; color: white; border-radius: 25px; width: 100%; border: none; }
    </style>
    """, unsafe_allow_html=True)

# --- CRASH-PROOF LOTTIE FUNCTION ---
def get_lottie(url):
    try:
        r = requests.get(url, timeout=3)
        return r.json() if r.status_code == 200 else None
    except:
        return None

def show_lottie(url, height=250, key=None):
    data = get_lottie(url)
    if data:
        st_lottie(data, height=height, key=key)
    else:
        st.write("❤️") # Fallback heart icon

# --- AUDIO FUNCTION ---
def play_audio(text, lang):
    try:
        tts = gTTS(text=text, lang=lang, slow=True)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        audio_b64 = base64.b64encode(fp.read()).decode()
        audio_tag = f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_b64}">'
        st.markdown(audio_tag, unsafe_allow_html=True)
    except:
        pass

# --- CONTENT DATABASE ---
languages = {
    "Sanskrit 🕉️": {
        "text": "प्रिये, किं भवती मां दंष्टुं इच्छति?", 
        "code": "hi", # Using Hindi voice for Sanskrit phonetics
        "note": "(Priye, kim bhavati mam damstum icchati?)"
    },
    "Hindi 🇮🇳": {
        "text": "बेबी, क्या तुम मुझे काटना चाहोगी?", 
        "code": "hi",
        "note": ""
    },
    "German 🇩🇪": {
        "text": "Baby, willst du mich beißen?", 
        "code": "de",
        "note": ""
    },
    "Spanish 🇪🇸": {
        "text": "Bebé, ¿quieres morderme?", 
        "code": "es",
        "note": ""
    },
    "Turkish 🇹🇷": {
        "text": "Bebeğim, beni ısırmak ister misin?", 
        "code": "tr",
        "note": ""
    }
}

# --- APP LAYOUT ---
show_lottie("https://lottie.host/8040409a-6756-4299-9759-33b68051a029/9f7l8fX7y9.json", key="main")

# Language Selection
selected_lang = st.selectbox("Choose a language for the message:", list(languages.keys()))

content = languages[selected_lang]

# Display Text
st.markdown(f"<h1>{content['text']}</h1>", unsafe_allow_html=True)
if content['note']:
    st.markdown(f"<p style='text-align:center; color:#ff758f;'>{content['note']}</p>", unsafe_allow_html=True)

# Autoplay Voice
play_audio(content['text'], content['code'])

st.write("---")

# Choice Buttons
c1, c2 = st.columns(2)
with c1:
    if st.button("YES! 😍"):
        st.balloons()
        st.success("I'm all yours! 😘")
        show_lottie("https://lottie.host/67702580-f00a-42fb-a7e8-e4b779a5e8c1/m8n8C0zE9Y.json", height=150, key="celeb")

with c2:
    if st.button("No 🥺"):
        st.warning("Error: 'No' is currently out of stock. Try 'YES'!")

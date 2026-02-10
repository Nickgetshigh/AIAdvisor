import streamlit as st
from streamlit_lottie import st_lottie
import requests
from gtts import gTTS
import base64
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="For My Bbygirl", page_icon="🔞", layout="centered")

# --- CSS STYLING ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(to bottom, #0f0c29, #302b63, #24243e); }
    .stButton>button {
        background-color: #ff0055;
        color: white;
        border-radius: 10px;
        height: 3.5em;
        width: 100%;
        border: none;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff5e91;
        box-shadow: 0px 0px 20px #ff0055;
    }
    .message-box {
        background: rgba(0, 0, 0, 0.6);
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #ff0055;
        text-align: center;
        color: #ffdae0;
        font-size: 22px;
        margin-bottom: 20px;
        font-family: 'Georgia', serif;
    }
    </style>
    """, unsafe_allow_html=True)

def play_audio(text, lang):
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        audio_b64 = base64.b64encode(fp.read()).decode()
        audio_tag = f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_b64}">'
        st.markdown(audio_tag, unsafe_allow_html=True)
    except: st.error("Audio Error")

st.markdown("<h1 style='text-align: center; color: #ff0055;'>Naughty Desires... 🔥</h1>", unsafe_allow_html=True)

# --- THE SPICY RHYMES ---
msg_data = {
    "English 🇬🇧": {
        "txt": "I know you want it, I know you’re wet. I’m the best mistake you haven’t made yet. Up and down, I’ll make you moan, I’m taking you to the danger zone.", 
        "code": "en-au" # Australian usually sounds deeper/more masculine
    },
    "Telugu 🇮🇳": {
        "txt": "Nee vanti vedi, naaku telusu... nee korika teerustha, idi na varusa. Paiki kindaki, ninnu tipputha... gichhi gichhi, ninnu munchutha.", 
        "code": "te"
    },
    "Urdu 🇵🇰": {
        "txt": "Tumhara badan garam hai, mera irada kharab... Raat bhar jagayenge, mitaenge har khwab. Upar niche, har jagah... Dunga tumhe asli maza.", 
        "code": "ur"
    },
    "Afghani (Dari) 🇦🇫": {
        "txt": "Badanat garm as, labat teshna... Bia pesham bacha, nako nakhra. Bala o payin, dar khedmatat... Mekonum emshab, qurbanat.", 
        "code": "fr" # Note: gTTS doesn't support Dari/Pashto natively. Using 'fr' or 'ar' as a placeholder or you can use English text with Afghani accent.
    },
    "Hindi 🇮🇳": {
        "txt": "Tadap rahi ho tum, mujhe sab pata hai... Mere sath bitao raat, yahi saza hai. Upar niche, round and round... Karege dhamaka, no other sound.", 
        "code": "hi"
    }
}

# --- LAYOUT ---
cols = st.columns(2)
for i, (name, info) in enumerate(msg_data.items()):
    with cols[i % 2]:
        if st.button(name):
            st.markdown(f'<div class="message-box">{info["txt"]}</div>', unsafe_allow_html=True)
            play_audio(info['txt'], info['code'])

st.markdown("<br>", unsafe_allow_html=True)

if st.button("READY FOR MORE? 😈"):
    st.snow()
    st.write("<h3 style='text-align: center; color: white;'>Check your DMs... I'm coming over.</h3>", unsafe_allow_html=True)

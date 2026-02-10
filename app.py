import streamlit as st
from streamlit_lottie import st_lottie
import requests
from gtts import gTTS
import base64
import io
import os
from pydub import AudioSegment

# --- PAGE CONFIG ---
st.set_page_config(page_title="For My Bbygirl", page_icon="🔞", layout="centered")

# --- FIX FOR FFPROBE/FFMPEG ---
# If running locally on Windows, point to your ffmpeg folder:
# AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"
# AudioSegment.ffprobe = r"C:\ffmpeg\bin\ffprobe.exe"

# --- CUSTOM ROMANTIC CSS ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(to bottom, #2c003e, #fe2851); }
    .stButton>button {
        background-color: #ff0055; color: white; border-radius: 20px;
        height: 3.5em; width: 100%; border: none;
        font-weight: bold; font-size: 16px; transition: 0.3s;
        box-shadow: 0px 4px 15px rgba(255, 0, 85, 0.4);
    }
    .stButton>button:hover { background-color: #ff4d6d; transform: translateY(-3px); }
    .message-box {
        background: rgba(0, 0, 0, 0.4); padding: 25px;
        border-radius: 20px; border: 1px solid #ff4d6d;
        text-align: center; color: #ffffff; font-size: 20px;
        font-family: 'Georgia', serif; line-height: 1.6;
        margin-bottom: 20px; font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BACKGROUND MUSIC ---
# This plays a subtle, sensual loop in the background
def play_bg_music():
    bg_music_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-17.mp3" # Smooth Lo-Fi example
    st.markdown(f"""
        <audio autoplay loop inline>
            <source src="{bg_music_url}" type="audio/mp3">
        </audio>
        """, unsafe_allow_html=True)

play_bg_music()

# --- UTILITY FUNCTIONS ---
def get_lottie(url):
    try:
        r = requests.get(url, timeout=3)
        return r.json() if r.status_code == 200 else None
    except: return None

def play_male_audio(text, lang):
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        temp_fp = io.BytesIO()
        tts.write_to_fp(temp_fp)
        temp_fp.seek(0)

        # Shift pitch to make it deep and male
        sound = AudioSegment.from_file(temp_fp, format="mp3")
        new_sample_rate = int(sound.frame_rate * 0.82) 
        low_pitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
        low_pitch_sound = low_pitch_sound.set_frame_rate(sound.frame_rate)

        out_fp = io.BytesIO()
        low_pitch_sound.export(out_fp, format="mp3")
        out_fp.seek(0)
        
        audio_b64 = base64.b64encode(out_fp.read()).decode()
        audio_tag = f'<audio autoplay src="data:audio/mp3;base64,{audio_b64}">'
        st.markdown(audio_tag, unsafe_allow_html=True)
    except Exception as e:
        st.error("Ensure FFmpeg is installed on your system path!")

# --- APP LAYOUT ---
lottie_main = get_lottie("https://lottie.host/8040409a-6756-4299-9759-33b68051a029/9f7l8fX7y9.json")
if lottie_main:
    st_lottie(lottie_main, height=250, key="main")

st.markdown("<h1 style='text-align: center; color: white;'>A Rhythm for You...</h1>", unsafe_allow_html=True)

# --- LYRICAL DATA ---
# Rhyme: Need me/Bby to me, Up and down/Round and round
lyric_txt = (
    "So you want me, and you need me... "
    "Come bby to me, right now, now, now. "
    "Bbygirl I'll take you up and down, "
    "Spinning your heart round and round."
)

msg_data = {
    "English 🇬🇧": {"txt": lyric_txt, "code": "en"},
    "Telugu 🇮🇳": {"txt": "నీకు నేను కావాలి, నీకు నా అవసరం ఉంది. ఇప్పుడే నా దగ్గరకు రా. నిన్ను పైకి కిందకి తీసుకెళ్తా, లోకాన్ని చుట్టూ తిప్పుతా.", "code": "te"},
    "Hindi 🇮🇳": {"txt": "तुम्हें मेरी चाहत है, तुम्हें मेरी ज़रूरत है. अभी मेरे पास आओ. मैं तुम्हें ऊपर-नीचे ले जाऊंगा, और गोल-गोल घुमाऊंगा।", "code": "hi"},
    "Spanish 🇪🇸": {"txt": "Me quieres y me necesitas. Ven a mí ahora mismo. Te llevaré de arriba abajo, dándote vueltas una y otra vez.", "code": "es"},
    "French 🇫🇷": {"txt": "Tu me veux, tu as besoin de moi. Viens à moi tout de suite. Je t'emmènerai de haut en bas, encore et encore.", "code": "fr"}
}

# --- BUTTON GRID ---
cols = st.columns(2)
for i, (name, info) in enumerate(msg_data.items()):
    with cols[i % 2]:
        if st.button(name):
            st.markdown(f'<div class="message-box">"{info["txt"]}"</div>', unsafe_allow_html=True)
            play_male_audio(info['txt'], info['code'])

st.markdown("<br>", unsafe_allow_html=True)

# --- THE RESPONSE ---
if st.button("CLAIM YOUR GIFT 🎁"):
    st.balloons()
    st.confetti()
    st.markdown("<h3 style='text-align: center; color: white;'>You're mine tonight. ❤️</h3>", unsafe_allow_html=True)

import streamlit as st
from streamlit_lottie import st_lottie
import requests
from gtts import gTTS
import base64
import io
from pydub import AudioSegment

# --- PAGE CONFIG ---
st.set_page_config(page_title="For My Bbygirl", page_icon="🔞", layout="centered")

# --- CUSTOM ROMANTIC CSS ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(to bottom, #ffafbd, #ffc3a0); }
    .stButton>button {
        background-color: #d63384; color: white; border-radius: 50px;
        height: 3em; width: 100%; border: 2px solid #ffffff;
        font-weight: bold; font-size: 18px; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #ff4d6d; transform: scale(1.05); }
    .message-box {
        background-color: rgba(255, 255, 255, 0.2); padding: 20px;
        border-radius: 15px; border: 1px solid white; text-align: center;
        color: white; font-size: 18px; margin-bottom: 20px; font-weight: bold;
    }
    hr { border: 1px solid #ffffff; }
    </style>
    """, unsafe_allow_html=True)

# --- UTILITY FUNCTIONS ---
def get_lottie(url):
    try:
        r = requests.get(url, timeout=3)
        return r.json() if r.status_code == 200 else None
    except: return None

def play_male_audio(text, lang):
    try:
        # 1. Generate normal TTS
        tts = gTTS(text=text, lang=lang, slow=False)
        temp_fp = io.BytesIO()
        tts.write_to_fp(temp_fp)
        temp_fp.seek(0)

        # 2. Use Pydub to lower the pitch (makes it sound male)
        sound = AudioSegment.from_file(temp_fp, format="mp3")
        
        # Lowering the sample rate shifts the pitch down
        new_sample_rate = int(sound.frame_rate * 0.85) # 0.8 to 0.9 is the "male" sweet spot
        low_pitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
        low_pitch_sound = low_pitch_sound.set_frame_rate(sound.frame_rate)

        # 3. Export to base64
        out_fp = io.BytesIO()
        low_pitch_sound.export(out_fp, format="mp3")
        out_fp.seek(0)
        
        audio_b64 = base64.b64encode(out_fp.read()).decode()
        audio_tag = f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_b64}">'
        st.markdown(audio_tag, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Audio Error: {e}")

# --- APP LAYOUT ---
lottie_main = get_lottie("https://lottie.host/8040409a-6756-4299-9759-33b68051a029/9f7l8fX7y9.json")
if lottie_main:
    st_lottie(lottie_main, height=300, key="main")

st.markdown("<h2 style='text-align: center; color: white;'>Press a button to hear me...</h2>", unsafe_allow_html=True)

# --- UPDATED LANGUAGE DATA ---
msg_data = {
    "English 🇬🇧": {"txt": "So you want me do you need me wanna fuck me come bby to me right now now now right now now now. Bbygirl I will take you up and down up and down round and round.", "code": "en"},
    "Telugu 🇮🇳": {"txt": "కాబట్టి మీకు నేను కావాలి, మీకు నా అవసరం ఉందా, నాతో కలవాలనుకుంటున్నారా, ఇప్పుడే నా దగ్గరకు రండి. బేబీ గర్ల్, నేను నిన్ను పైకి కిందకి, చుట్టూ తిప్పుతాను.", "code": "te"},
    "Hindi 🇮🇳": {"txt": "तो तुम मुझे चाहती हो, क्या तुम्हें मेरी ज़रूरत है, क्या तुम मेरे साथ हमबिस्तर होना चाहती हो, अभी मेरे पास आओ। बेबी गर्ल, मैं तुम्हें ऊपर-नीचे और गोल-गोल घुमाऊंगा।", "code": "hi"},
    "Spanish 🇪🇸": {"txt": "Así que me quieres, ¿me necesitas, quieres follarme? ven a mí ahora mismo. Bbygirl, te llevaré de arriba abajo y daremos vueltas.", "code": "es"},
    "French 🇫🇷": {"txt": "Alors tu me veux, tu as besoin de moi, tu veux me baiser ? viens à moi tout de suite. Bbygirl, je t'emmènerai de haut en bas et ferai le tour.", "code": "fr"},
    "German 🇩🇪": {"txt": "Du willst mich also, brauchst du mich, willst du mich ficken? komm jetzt sofort zu mir. Bbygirl, ich werde dich auf und ab führen, rundherum.", "code": "de"},
    "Korean 🇰🇷": {"txt": "그래서 넌 나를 원해, 내가 필요해, 나랑 섹스하고 싶어? 지금 당장 내게로 와. Bbygirl, 널 위아래로, 빙글빙글 데려갈게.", "code": "ko"}
}

# --- BUTTON GRID ---
cols = st.columns(2)
for i, (name, info) in enumerate(msg_data.items()):
    with cols[i % 2]:
        if st.button(name):
            st.markdown(f'<div class="message-box">{info["txt"]}</div>', unsafe_allow_html=True)
            play_male_audio(info['txt'], info['code'])

st.markdown("<br><hr>", unsafe_allow_html=True)

# --- THE RESPONSE ---
c1, c2 = st.columns(2)
with c1:
    if st.button("YES! 😍"):
        st.balloons()
        lottie_yes = get_lottie("https://lottie.host/67702580-f00a-42fb-a7e8-e4b779a5e8c1/m8n8C0zE9Y.json")
        if lottie_yes: st_lottie(lottie_yes, height=200, key="yes")

with c2:
    if st.button("No 🥺"):
        st.write("Nice try, but 'No' is disabled today! ❤️")

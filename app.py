import streamlit as st
from streamlit_lottie import st_lottie
import requests
from gtts import gTTS
import base64
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="Deep Desires", page_icon="🐬", layout="centered")

# --- BACKGROUND & MUSIC SETUP ---
def setup_environment():
    # Background Music (Low Volume)
    music_url = "https://www.pagalworld.com.sb/files/download/id/68172" 
    # Video Background (Dolphins)
    video_url = "https://assets.mixkit.co/videos/preview/mixkit-dolphins-swimming-underwater-in-the-ocean-1561-large.mp4"
    
    st.markdown(f"""
        <style>
        #bg-video {{
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%;
            min-height: 100%;
            z-index: -1;
            filter: brightness(30%);
        }}
        .stApp {{
            background: rgba(0,0,0,0);
        }}
        .stButton>button {{
            background: linear-gradient(45deg, #0077be, #ff0055);
            color: white;
            border-radius: 12px;
            height: 4em;
            width: 100%;
            border: none;
            font-weight: bold;
            font-size: 15px;
            box-shadow: 0px 4px 15px rgba(255, 0, 85, 0.3);
        }}
        .message-box {{
            background: rgba(0, 0, 0, 0.8);
            padding: 20px;
            border-radius: 15px;
            border: 1px solid #ff0055;
            text-align: center;
            color: #ff4d88;
            font-size: 20px;
            margin-bottom: 20px;
            font-family: 'Arial Black', Gadget, sans-serif;
        }}
        </style>
        
        <video autoplay muted loop id="bg-video">
            <source src="{video_url}" type="video/mp4">
        </video>
        
        <audio id="bg-music" autoplay loop>
            <source src="{music_url}" type="audio/mp3">
        </audio>
        <script>
            var audio = document.getElementById("bg-music");
            audio.volume = 0.1;
        </script>
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
    except: st.error("Voice Error")

# --- APP START ---
setup_environment()
st.markdown("<h1 style='text-align: center; color: white;'>🐬 Wet & Wild</h1>", unsafe_allow_html=True)

# --- THE VULGAR RHYTHMIC RHYMES ---
# Combining your specific request with explicit slang and rhymes
msg_data = {
    "English 🇬🇧": ("Do you want me? Wanna fuck me? Aaja bby mere naal right now now now. I wanna lick you raw, make you scream for more, then fuck you hard until you hit the floor.", "en-uk"),
    "Hindi/Urdu 🇮🇳": ("Aaja bby mere naal right now now now. Teri choot chatni hai, tujhe pelna hai... aaj raat tere badan se khelna hai. Garm kar mujhe, phir zor se le... mere lund pe tu maze se reh.", "hi"),
    "Telugu 🇮🇳": ("Aaja bby mere naal right now now now. Nee rasalu naaku kavali, nee pooku nenu cheekali. Paiki kindaki ninnu dengaali... nee gola nenu vinali.", "te"),
    "Spanish 🇪🇸": ("¿Me quieres? ¿Quieres follarme? Ven conmigo ahora mismo. Quiero lamerte toda y luego follarte tan duro que no olvides mi nombre.", "es"),
    "Punjabi 🇮🇳": ("Aaja bby mere naal right now now now. Teri garm jawani nu nasha pilada... tenu sutt ke nange kar ke maza dikhada. Chak de phatte, hor zor naal!", "hi"),
    "Korean 🇰🇷": ("Nal wonhae? Na-rang seksu-hago sipeo? Jigeum dangjang wa. Neo-ui momeul halttgo sip-eo, geurigo sege bakh-eulgeoya. Gyesokhae.", "ko"),
    "Chinese 🇨🇳": ("Nǐ xiǎng yào wǒ ma? Xiǎng gēn wǒ shàngchuáng ma? Xiànzài jiù lái. Wǒ yào tiǎn nǐ, rán hòu yònglì cào nǐ. Shàng xià bù tíng.", "zh-cn"),
    "Afghani (Dari)": ("Bia pesham right now now now. Labat ra mekhum, badant ra mekhum. Emshab tura qurban mekonum, ba zor bakhuda.", "hi")
}

# --- 2-COLUMN GRID ---
keys = list(msg_data.keys())
for i in range(0, len(keys), 2):
    col1, col2 = st.columns(2)
    with col1:
        l1 = keys[i]
        if st.button(l1):
            st.session_state['msg'] = msg_data[l1][0]
            play_audio(msg_data[l1][0], msg_data[l1][1])
    with col2:
        if i + 1 < len(keys):
            l2 = keys[i+1]
            if st.button(l2):
                st.session_state['msg'] = msg_data[l2][0]
                play_audio(msg_data[l2][0], msg_data[l2][1])

# --- MESSAGE DISPLAY ---
if 'msg' in st.session_state:
    st.markdown(f'<div class="message-box">{st.session_state["msg"]}</div>', unsafe_allow_html=True)

st.markdown("<br><hr style='border-color: #0077be;'>", unsafe_allow_html=True)

if st.button("I'M WET... TAKE ME! 💦"):
    st.balloons()
    st.markdown("<h2 style='text-align: center; color: #ff0055;'>Spread them. I'm coming.</h2>", unsafe_allow_html=True)

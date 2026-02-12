import streamlit as st
from streamlit_lottie import st_lottie
import requests
from gtts import gTTS
import base64
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="Dangerous Desires", page_icon="🐬", layout="centered")

# --- BACKGROUND & MUSIC SETUP ---
def setup_environment():
    # Background Music (Low Volume Bollywood)
    music_url = "https://www.pagalworld.com.sb/files/download/id/68172" 
    # Video Background (Dolphins)
    video_url = "https://assets.mixkit.co/videos/preview/mixkit-dolphins-swimming-underwater-in-the-ocean-1561-large.mp4"
    
    st.markdown(f"""
        <style>
        #bg-video {{
            position: fixed; right: 0; bottom: 0;
            min-width: 100%; min-height: 100%;
            z-index: -1; filter: brightness(35%) contrast(120%);
        }}
        .stApp {{ background: rgba(0,0,0,0); }}
        
        /* Button Styling */
        .stButton>button {{
            color: white;
            border-radius: 8px;
            height: 3em;
            width: 100%;
            border: 1px solid #00f2ff;
            font-weight: bold;
            transition: 0.3s;
        }}
        /* Vocal 1 Style */
        div[data-testid="stVerticalBlock"] > div:nth-child(1) button {{
            background: linear-gradient(45deg, #ff0055, #800020);
        }}
        /* Vocal 2 Style (Akon) */
        div[data-testid="stVerticalBlock"] > div:nth-child(2) button {{
            background: linear-gradient(45deg, #0077be, #001f3f);
        }}
        
        .message-box {{
            background: rgba(0, 0, 0, 0.85);
            padding: 20px;
            border-radius: 15px;
            border: 2px solid #00f2ff;
            text-align: center;
            color: #ff4d88;
            font-size: 22px;
            margin-top: 20px;
            text-shadow: 0px 0px 10px #ff0055;
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
            audio.volume = 0.05;
        </script>
        """, unsafe_allow_html=True)

def play_audio(text, lang, is_akon=False):
    if is_akon:
        # Link to a clip of Akon - Dangerous
        akon_url = "https://www.myinstants.com/media/sounds/akon-dangerous.mp3"
        st.markdown(f'<audio autoplay="true" src="{akon_url}"></audio>', unsafe_allow_html=True)
    else:
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
st.markdown("<h1 style='text-align: center; color: #00f2ff;'>🐬 DANGEROUS WHISPERS</h1>", unsafe_allow_html=True)

# --- THE DATA ---
msg_data = {
    "English 🇬🇧": ("Do you want me? Wanna fuck me? Aaja bby mere naal right now now now. I wanna lick you raw, make you moan for more, then fuck you hard until you hit the floor.", "en-uk"),
    "Hindi 🇮🇳": ("Aaja bby mere naal right now now now. Teri choot chatni hai, tujhe pelna hai. Garm kar mujhe, mere lund pe tu maze se reh.", "hi"),
    "Urdu 🇵🇰": ("Aaja bby mere naal right now now now. Be-sharm nigaahein, garm saansein. Kapre utaaro, mujhe apni tapan dikhao.", "ur"),
    "Telugu 🇮🇳": ("Aaja bby mere naal right now now now. Nee rasalu naaku kavali, nee pooku nenu cheekali. Paiki kindaki ninnu dengaali.", "te"),
    "Spanish 🇪🇸": ("¿Me quieres? ¿Quieres follarme? Aaja bby mere naal right now. Quiero lamerte toda y luego follarte tan duro.", "es"),
    "Korean 🇰🇷": ("Nal wonhae? Na-rang seksu-hago sipeo? Aaja bby mere naal right now. Neo-ui momeul halttgo sip-eo, geurigo bakh-eulgeoya.", "ko"),
    "Chinese 🇨🇳": ("Nǐ xiǎng yào wǒ ma? Xiǎng gēn wǒ shàngchuáng ma? Aaja bby mere naal right now. Wǒ yào tiǎn nǐ, rán hòu cào nǐ.", "zh-cn"),
    "Punjabi 🇮🇳": ("Aaja bby mere naal right now now now. Teri garm jawani nu nasha pilada. Tenu sutt ke nange kar ke maza dikhada.", "hi")
}

# --- 2-COLUMN GRID (2 BUTTONS PER LANG) ---
keys = list(msg_data.keys())
for i in range(0, len(keys), 2):
    col1, col2 = st.columns(2)
    
    with col1:
        lang = keys[i]
        st.write(f"**{lang}**")
        if st.button(f"Dirty Vocal 1", key=f"v1_{i}"):
            st.session_state['msg'] = msg_data[lang][0]
            play_audio(msg_data[lang][0], msg_data[lang][1])
        if st.button(f"Akon - Dangerous", key=f"v2_{i}"):
            st.session_state['msg'] = "🔥 That girl is so dangerous! 🔥"
            play_audio("", "", is_akon=True)

    with col2:
        if i + 1 < len(keys):
            lang = keys[i+1]
            st.write(f"**{lang}**")
            if st.button(f"Dirty Vocal 1", key=f"v1_{i+1}"):
                st.session_state['msg'] = msg_data[lang][0]
                play_audio(msg_data[lang][0], msg_data[lang][1])
            if st.button(f"Akon - Dangerous", key=f"v2_{i+1}"):
                st.session_state['msg'] = "🔥 That girl is so dangerous! 🔥"
                play_audio("", "", is_akon=True)

# --- MESSAGE DISPLAY ---
if 'msg' in st.session_state:
    st.markdown(f'<div class="message-box">{st.session_state["msg"]}</div>', unsafe_allow_html=True)

st.markdown("<br><hr style='border-color: #00f2ff;'>", unsafe_allow_html=True)

if st.button("I'M ALL YOURS... 🔥"):
    st.snow()
    st.markdown("<h2 style='text-align: center; color: #ff0055;'>The bed is ready. Don't keep me waiting.</h2>", unsafe_allow_html=True)

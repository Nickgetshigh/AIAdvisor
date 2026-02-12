import streamlit as st
from streamlit_lottie import st_lottie
import requests
from gtts import gTTS
import base64
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="Bitch I'm a Cow", page_icon="🐄", layout="centered")

# --- BACKGROUND & MUSIC SETUP ---
def setup_environment():
    # Background Music (Very Low Bollywood Mix)
    music_url = "https://www.pagalworld.com.sb/files/download/id/68172" 
    # Video Background (Dolphins)
    video_url = "https://assets.mixkit.co/videos/preview/mixkit-dolphins-swimming-underwater-in-the-ocean-1561-large.mp4"
    
    st.markdown(f"""
        <style>
        #bg-video {{
            position: fixed; right: 0; bottom: 0;
            min-width: 100%; min-height: 100%;
            z-index: -1; filter: brightness(30%) sepia(20%);
        }}
        .stApp {{ background: rgba(0,0,0,0); }}
        
        /* Lyrics Styling */
        .lyrics-container {{
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            color: #f8f9fa;
            font-style: italic;
            border: 1px dashed #ff0055;
            margin-bottom: 30px;
        }}

        .stButton>button {{
            color: white;
            border-radius: 50px;
            height: 3.5em;
            width: 100%;
            font-weight: bold;
            transition: 0.4s;
            border: none;
        }}
        /* Vocal 1 - Dirty */
        div[data-testid="stVerticalBlock"] > div:nth-child(2) button {{
            background: linear-gradient(45deg, #ff0055, #4a00e0);
        }}
        /* Vocal 2 - Doja Cat */
        div[data-testid="stVerticalBlock"] > div:nth-child(3) button {{
            background: linear-gradient(45deg, #00dbde, #fc00ff);
        }}
        
        .message-box {{
            background: rgba(0, 0, 0, 0.9);
            padding: 20px;
            border-radius: 15px;
            border: 2px solid #00dbde;
            text-align: center;
            color: #ff0055;
            font-size: 20px;
            font-weight: bold;
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

def play_audio(text, lang, is_doja=False):
    if is_doja:
        # High-quality clip of Doja Cat - Mooo!
        doja_url = "https://www.myinstants.com/media/sounds/doja-cat-mooo-official-video.mp3"
        st.markdown(f'<audio autoplay="true" src="{doja_url}"></audio>', unsafe_allow_html=True)
    else:
        try:
            tts = gTTS(text=text, lang=lang, slow=False)
            fp = io.BytesIO()
            tts.write_to_fp(fp)
            fp.seek(0)
            audio_b64 = base64.b64encode(fp.read()).decode()
            audio_tag = f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_b64}">'
            st.markdown(audio_tag, unsafe_allow_html=True)
        except: st.error("Voice sync failed.")

# --- APP START ---
setup_environment()

st.markdown("<h1 style='text-align: center; color: white;'>💦 MOOO-PHIN VIBES 🐬</h1>", unsafe_allow_html=True)

# --- STATIC LYRICS (FIRST STANZA) ---
st.markdown("""
<div class="lyrics-container">
    <p>Bitch, I'm a cow, bitch, I'm a cow</p>
    <p>I'm not a cat, I don't say mew</p>
    <p>Bitch, I'm a cow, bitch, I'm a cow</p>
    <p>Bitch, I'm a cow, bitch, I'm a cow</p>
</div>
""", unsafe_allow_html=True)

# --- THE DATA ---
msg_data = {
    "English 🇬🇧": ("Do you want me? Wanna fuck me? Aaja bby mere naal right now. I wanna lick you raw, make you moan for more, then fuck you hard.", "en-uk"),
    "Hindi 🇮🇳": ("Aaja bby mere naal right now. Teri choot chatni hai, tujhe pelna hai. Garm kar mujhe, mere lund pe tu maze se reh.", "hi"),
    "Urdu 🇵🇰": ("Aaja bby mere naal right now. Be-sharm nigaahein, garm saansein. Kapre utaaro, mujhe apni tapan dikhao.", "ur"),
    "Telugu 🇮🇳": ("Aaja bby mere naal right now now now. Nee rasalu naaku kavali, nee pooku nenu cheekali. Paiki kindaki ninnu dengaali.", "te"),
    "Spanish 🇪🇸": ("¿Me quieres? ¿Quieres follarme? Aaja bby mere naal right now. Quiero lamerte toda y luego follarte.", "es"),
    "Korean 🇰🇷": ("Nal wonhae? Na-rang seksu-hago sipeo? Aaja bby mere naal right now. Neo-ui momeul halttgo sip-eo.", "ko"),
    "Chinese 🇨🇳": ("Nǐ xiǎng yào wǒ ma? Xiǎng gēn wǒ shàngchuáng ma? Aaja bby mere naal right now. Wǒ yào tiǎn nǐ.", "zh-cn"),
    "Punjabi 🇮🇳": ("Aaja bby mere naal right now now now. Teri garm jawani nu nasha pilada. Tenu nange kar ke maza dikhada.", "hi")
}

# --- 2-COLUMN GRID ---
keys = list(msg_data.keys())
for i in range(0, len(keys), 2):
    col1, col2 = st.columns(2)
    
    with col1:
        lang = keys[i]
        st.write(f"**{lang}**")
        if st.button(f"Dirty Vocal", key=f"v1_{i}"):
            st.session_state['msg'] = msg_data[lang][0]
            play_audio(msg_data[lang][0], msg_data[lang][1])
        if st.button(f"Mooo! - Doja", key=f"v2_{i}"):
            st.session_state['msg'] = "🐄 MOOO! Bitch I'm a cow! 🐄"
            play_audio("", "", is_doja=True)

    with col2:
        if i + 1 < len(keys):
            lang = keys[i+1]
            st.write(f"**{lang}**")
            if st.button(f"Dirty Vocal", key=f"v1_{i+1}"):
                st.session_state['msg'] = msg_data[lang][0]
                play_audio(msg_data[lang][0], msg_data[lang][1])
            if st.button(f"Mooo! - Doja", key=f"v2_{i+1}"):
                st.session_state['msg'] = "🐄 MOOO! Bitch I'm a cow! 🐄"
                play_audio("", "", is_doja=True)

# --- MESSAGE DISPLAY ---
if 'msg' in st.session_state:
    st.markdown(f'<div class="message-box">{st.session_state["msg"]}</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
if st.button("GET MILKED? 🍼"):
    st.balloons()
    st.write("<h3 style='text-align: center; color: white;'>I'm ready for the farm. See you in the barn.</h3>", unsafe_allow_html=True)

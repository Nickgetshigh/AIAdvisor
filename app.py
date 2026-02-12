import streamlit as st
from gtts import gTTS
import base64
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="I F*cking Love You", page_icon="🐬", layout="centered")

# --- BACKGROUND & MUSIC SETUP ---
def setup_environment():
    music_url = "https://www.pagalworld.com.sb/files/download/id/68172" 
    video_url = "https://assets.mixkit.co/videos/preview/mixkit-dolphins-swimming-underwater-in-the-ocean-1561-large.mp4"
    
    st.markdown(f"""
        <style>
        #bg-video {{
            position: fixed; right: 0; bottom: 0;
            min-width: 100%; min-height: 100%;
            z-index: -1; filter: brightness(25%);
        }}
        .stApp {{ background: rgba(0,0,0,0); }}
        
        .lyrics-container {{
            background: rgba(0, 0, 0, 0.5);
            border-radius: 15px;
            padding: 15px;
            text-align: center;
            color: #00f2ff;
            font-size: 14px;
            border: 1px solid #ff0055;
            margin-bottom: 20px;
        }}

        .stButton>button {{
            color: white;
            border-radius: 8px;
            height: 3em;
            width: 100%;
            font-weight: bold;
            font-size: 12px;
            border: none;
            margin-bottom: 5px;
        }}
        /* Dirty Vocal */
        div[data-testid="stVerticalBlock"] button[key^="d_"] {{ background: linear-gradient(45deg, #ff0055, #800020); }}
        /* Mooo! */
        div[data-testid="stVerticalBlock"] button[key^="s_"] {{ background: linear-gradient(45deg, #00dbde, #2193b0); }}
        /* IFLY */
        div[data-testid="stVerticalBlock"] button[key^="i_"] {{ background: linear-gradient(45deg, #fceabb, #f8b500); color: black; }}
        
        .message-box {{
            background: rgba(0, 0, 0, 0.9);
            padding: 20px;
            border-radius: 15px;
            border: 2px solid #f8b500;
            text-align: center;
            color: #ffffff;
            font-size: 18px;
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

setup_environment()
st.markdown("<h1 style='text-align: center; color: white;'>💦 WET WHISPERS 🐬</h1>", unsafe_allow_html=True)

# --- THE DATA ---
msg_data = {
    "English 🇬🇧": {
        "code": "en-uk",
        "dirty": "Do you want me? Wanna fuck me? Aaja bby mere naal right now. I wanna lick you raw, make you moan for more.",
        "song": "Bitch I am a cow, bitch I am a cow. I am not a cat, I do not say mew.",
        "ifly": "This my baby, this my star. Only thing I want is what you are. Girl, you're so perfect. I f-ing love you."
    },
    "Hindi 🇮🇳": {
        "code": "hi",
        "dirty": "Aaja bby mere naal right now. Teri choot chatni hai, tujhe pelna hai. Garm kar mujhe, mere lund pe tu maze se reh.",
        "song": "Kutti, mein ek gaay hoon. Mein billi nahi hoon, mein mew nahi kehti.",
        "ifly": "Ye meri jaan hai, ye mera sitara hai. Mujhe sirf tum chahiye. Tum bilkul sahi ho. Main tumse bahut pyaar karta hoon."
    },
    "Telugu 🇮🇳": {
        "code": "te",
        "dirty": "Aaja bby mere naal right now. Nee rasalu naaku kavali, nee pooku nenu cheekali. Paiki kindaki ninnu dengaali.",
        "song": "Lanja, nenu oka aavu nu. Nenu pilli ni kaadu, nenu mew ananu.",
        "ifly": "Idhi naa bangaram, idhi naa nakshatram. Naku nuvvu thappa emi vaddu. Nuvvu chala perfect. Nenu ninnu pichiga premisthunnanu."
    },
    "Spanish 🇪🇸": {
        "code": "es",
        "dirty": "¿Me quieres? ¿Quieres follarme? Aaja bby mere naal right now. Quiero lamerte toda.",
        "song": "Perra, soy una vaca. No soy un gato, no digo miau.",
        "ifly": "Esta es mi nena, esta es mi estrella. Solo quiero lo que eres. Eres tan perfecta. Te amo jodidamente."
    },
    "Urdu 🇵🇰": {
        "code": "ur",
        "dirty": "Aaja bby mere naal right now. Be-sharm nigaahein, garm saansein. Kapre utaaro.",
        "song": "Kutti, mein ek gaay hoon. Mein billi nahi hoon.",
        "ifly": "Ye meri jaan hai, ye mera sitara hai. Mujhe sirf tumhari zarurat hai. Tum bilkul mukammal ho. Mujhe tumse mohabbat hai."
    },
    "Korean 🇰🇷": {
        "code": "ko",
        "dirty": "Nal wonhae? Na-rang seksu-hago sipeo? Aaja bby mere naal right now.",
        "song": "Nappeun nyeon, naneun so-ya. Naneun goyang-iga aniya.",
        "ifly": "Nae sarang, nae byeol. Naega wonhaneun geon neo ppuniya. Neon neomu wanbyeokhae. Jinshimeuro saranghae."
    }
}

# --- 2-COLUMN GRID WITH 3 BUTTONS EACH ---
keys = list(msg_data.keys())
for i in range(0, len(keys), 2):
    col1, col2 = st.columns(2)
    
    for idx, col in enumerate([col1, col2]):
        if i + idx < len(keys):
            lang = keys[i + idx]
            with col:
                st.write(f"**{lang}**")
                if st.button(f"Dirty Vocal", key=f"d_{i+idx}"):
                    st.session_state['msg'] = msg_data[lang]['dirty']
                    play_audio(msg_data[lang]['dirty'], msg_data[lang]['code'])
                if st.button(f"Mooo! (Local)", key=f"s_{i+idx}"):
                    st.session_state['msg'] = msg_data[lang]['song']
                    play_audio(msg_data[lang]['song'], msg_data[lang]['code'])
                if st.button(f"IFLY (Bazzi)", key=f"i_{i+idx}"):
                    st.session_state['msg'] = msg_data[lang]['ifly']
                    play_audio(msg_data[lang]['ifly'], msg_data[lang]['code'])

# --- MESSAGE BOX ---
if 'msg' in st.session_state:
    st.markdown(f'<div class="message-box">{st.session_state["msg"]}</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
if st.button("STILL THIRSTY? 🔥"):
    st.balloons()
    st.write("<h3 style='text-align: center; color: white;'>I'm ready for whatever comes next.</h3>", unsafe_allow_html=True)

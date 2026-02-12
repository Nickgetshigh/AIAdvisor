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
    music_url = "https://www.pagalworld.com.sb/files/download/id/68172" 
    video_url = "https://assets.mixkit.co/videos/preview/mixkit-dolphins-swimming-underwater-in-the-ocean-1561-large.mp4"
    
    st.markdown(f"""
        <style>
        #bg-video {{
            position: fixed; right: 0; bottom: 0;
            min-width: 100%; min-height: 100%;
            z-index: -1; filter: brightness(30%);
        }}
        .stApp {{ background: rgba(0,0,0,0); }}
        
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
        /* Dirty Vocal Button Style */
        div[data-testid="stVerticalBlock"] > div:nth-child(2) button {{
            background: linear-gradient(45deg, #ff0055, #4a00e0);
        }}
        /* Localized Song Button Style */
        div[data-testid="stVerticalBlock"] > div:nth-child(3) button {{
            background: linear-gradient(45deg, #00dbde, #2193b0);
        }}
        
        .message-box {{
            background: rgba(0, 0, 0, 0.9);
            padding: 20px;
            border-radius: 15px;
            border: 2px solid #00dbde;
            text-align: center;
            color: #ff0055;
            font-size: 18px;
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

def play_audio(text, lang):
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

# --- STATIC LYRICS DISPLAY ---
st.markdown("""
<div class="lyrics-container">
    <p>Bitch, I'm a cow, bitch, I'm a cow</p>
    <p>I'm not a cat, I don't say mew</p>
    <p>Bitch, I'm a cow, bitch, I'm a cow</p>
</div>
""", unsafe_allow_html=True)

# --- THE DATA (DIRTY & LOCALIZED SONG) ---
msg_data = {
    "English 🇬🇧": {
        "dirty": "Do you want me? Wanna fuck me? Aaja bby mere naal right now. I wanna lick you raw, make you moan for more.",
        "song": "Bitch I am a cow, bitch I am a cow. I am not a cat, I do not say mew. Bitch I am a cow.",
        "code": "en-uk"
    },
    "Hindi 🇮🇳": {
        "dirty": "Aaja bby mere naal right now. Teri choot chatni hai, tujhe pelna hai. Garm kar mujhe, mere lund pe tu maze se reh.",
        "song": "Kutti, mein ek gaay hoon. Mein billi nahi hoon, mein mew nahi kehti. Kutti, mein ek gaay hoon.",
        "code": "hi"
    },
    "Urdu 🇵🇰": {
        "dirty": "Aaja bby mere naal right now. Be-sharm nigaahein, garm saansein. Kapre utaaro, mujhe apni tapan dikhao.",
        "song": "Kutti, mein ek gaay hoon. Mein billi nahi hoon, mein mew nahi kehti. Kutti, mein ek gaay hoon.",
        "code": "ur"
    },
    "Telugu 🇮🇳": {
        "dirty": "Aaja bby mere naal right now. Nee rasalu naaku kavali, nee pooku nenu cheekali. Paiki kindaki ninnu dengaali.",
        "song": "Lanja, nenu oka aavu nu. Nenu pilli ni kaadu, nenu mew ananu. Lanja, nenu oka aavu nu.",
        "code": "te"
    },
    "Spanish 🇪🇸": {
        "dirty": "¿Me quieres? ¿Quieres follarme? Aaja bby mere naal right now. Quiero lamerte toda y luego follarte.",
        "code": "es",
        "song": "Perra, soy una vaca. No soy un gato, no digo miau. Perra, soy una vaca."
    },
    "Korean 🇰🇷": {
        "dirty": "Nal wonhae? Na-rang seksu-hago sipeo? Aaja bby mere naal right now. Neo-ui momeul halttgo sip-eo.",
        "code": "ko",
        "song": "Nappeun nyeon, naneun so-ya. Naneun goyang-iga aniya, mew-rago haji ana. Nappeun nyeon, naneun so-ya."
    },
    "Chinese 🇨🇳": {
        "dirty": "Nǐ xiǎng yào wǒ ma? Xiǎng gēn wǒ shàngchuáng ma? Aaja bby mere naal right now. Wǒ yào tiǎn nǐ.",
        "code": "zh-cn",
        "song": "Biǎozi, wǒ shì yī tiáo niú. Wǒ bùshì māo, wǒ bù huì miāo miāo jiào. Biǎozi, wǒ shì yī tiáo niú."
    },
    "Punjabi 🇮🇳": {
        "dirty": "Aaja bby mere naal right now now now. Teri garm jawani nu nasha pilada. Tenu nange kar ke maza dikhada.",
        "code": "hi",
        "song": "Kuttiye, main ik gaan haan. Main billi nahi haan, main mew nahi kehndi. Kuttiye, main ik gaan haan."
    }
}

# --- 2-COLUMN GRID ---
keys = list(msg_data.keys())
for i in range(0, len(keys), 2):
    col1, col2 = st.columns(2)
    
    with col1:
        lang = keys[i]
        st.write(f"**{lang}**")
        if st.button(f"Dirty Vocal", key=f"d_{i}"):
            st.session_state['msg'] = msg_data[lang]['dirty']
            play_audio(msg_data[lang]['dirty'], msg_data[lang]['code'])
        if st.button(f"Mooo! (Local)", key=f"s_{i}"):
            st.session_state['msg'] = msg_data[lang]['song']
            play_audio(msg_data[lang]['song'], msg_data[lang]['code'])

    with col2:
        if i + 1 < len(keys):
            lang = keys[i+1]
            st.write(f"**{lang}**")
            if st.button(f"Dirty Vocal", key=f"d_{i+1}"):
                st.session_state['msg'] = msg_data[lang]['dirty']
                play_audio(msg_data[lang]['dirty'], msg_data[lang]['code'])
            if st.button(f"Mooo! (Local)", key=f"s_{i+1}"):
                st.session_state['msg'] = msg_data[lang]['song']
                play_audio(msg_data[lang]['song'], msg_data[lang]['code'])

# --- MESSAGE DISPLAY ---
if 'msg' in st.session_state:
    st.markdown(f'<div class="message-box">{st.session_state["msg"]}</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
if st.button("READY TO GET DIRTY? 🍼"):
    st.balloons()
    st.write("<h3 style='text-align: center; color: white;'>Check your DMs... let's go.</h3>", unsafe_allow_html=True)

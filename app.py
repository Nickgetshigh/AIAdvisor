import streamlit as st
from streamlit_lottie import st_lottie
import requests
from gtts import gTTS
import base64
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="Private Session", page_icon="🔥", layout="centered")

# --- UI & MUSIC SETUP ---
def add_bg_music():
    # Using a royalty-free rhythmic/sexy lofi beat
    music_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3" 
    st.markdown(f"""
        <audio autoplay loop inline>
            <source src="{music_url}" type="audio/mp3">
        </audio>
        """, unsafe_allow_html=True)

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #000000, #1a0005, #33000d); }
    .stButton>button {
        background: linear-gradient(45deg, #ff0055, #800020);
        color: white;
        border-radius: 8px;
        height: 4em;
        width: 100%;
        border: 1px solid #ff4d88;
        font-weight: bold;
        font-size: 16px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .stButton>button:hover {
        box-shadow: 0px 0px 25px #ff0055;
        transform: scale(1.02);
        color: #ffd1df;
    }
    .message-box {
        background: rgba(20, 20, 20, 0.85);
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #ff0055;
        text-align: center;
        color: #ffb3c6;
        font-size: 19px;
        margin-bottom: 15px;
        line-height: 1.4;
    }
    h1, h2 { text-shadow: 2px 2px 10px #ff0055; }
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
    except: st.error("Voice sync failed.")

# --- APP START ---
add_bg_music()
st.markdown("<h1 style='text-align: center; color: white;'>Naughty Whispers</h1>", unsafe_allow_html=True)

# --- DIRTY RHYMES DATA ---
# Using 'en-uk' and 'en-au' for masculine-leaning tones where possible
msg_data = {
    "English 🇬🇧": ("Harder and faster, do as I say. I’m gonna make you crave me all day. Up on the bed, down on the floor. I'll make you scream and beg for more.", "en-uk"),
    "Telugu 🇮🇳": ("Nee nadumu vonpu, naaku telusu... naa korika teerchu, idi naa varusa. Cheekatilo ninnu gichhi gichhi... pichhi ekkista, ninnu munchi.", "te"),
    "Urdu 🇵🇰": ("Raat hai jawaan, badan hai nanga... Karunga wo kaam, jo hai danga. Upar niche, har ek pal... Dunga sukoon, aaj aur kal.", "ur"),
    "Spanish 🇪🇸": ("Te quiero morder, te quiero tocar... En mi cama te voy a castigar. Arriba y abajo, sin descansar... Tus gemidos me van a encantar.", "es"),
    "Chinese 🇨🇳": ("Wǒ yào nǐ de shēntǐ, wǒ yào nǐ de hǎn... Zài wǒ de kuàngyě lǐ, nǐ bùnéng fǎn. Shàng shàng xià xià, wǒ bù huì tíng... Ràng nǐ de línghún, wèi wǒ ér míng.", "zh-cn"),
    "Korean 🇰🇷": ("Neo-ui momeul wonhae, nareul bwa... Naega neoreul michige halkkeoya. Wi araero, gyesokhae... Neon nae kkeoya, gajyeobwa.", "ko"),
    "Hindi 🇮🇳": ("Garmi hai badan mein, maza aayega... Jab mera haath, tere niche jayega. Round and round, hum ghoomenge... Tere honton ko, hum choomenge.", "hi"),
    "Afghani (Phonetic)": ("Labat teshna, badant garm... Mekonum emshab, khodeta narm. Bala o payin, nako nakhra... Bia pesham, bakhuda.", "en-au") 
}

# --- 2-COLUMN GRID ---
keys = list(msg_data.keys())
for i in range(0, len(keys), 2):
    col1, col2 = st.columns(2)
    
    # Language 1
    with col1:
        lang1 = keys[i]
        txt1, code1 = msg_data[lang1]
        if st.button(lang1):
            st.session_state['active_msg'] = txt1
            play_audio(txt1, code1)
            
    # Language 2
    with col2:
        if i + 1 < len(keys):
            lang2 = keys[i+1]
            txt2, code2 = msg_data[lang2]
            if st.button(lang2):
                st.session_state['active_msg'] = txt2
                play_audio(txt2, code2)

# --- MESSAGE DISPLAY ---
if 'active_msg' in st.session_state:
    st.markdown(f'<div class="message-box">{st.session_state["active_msg"]}</div>', unsafe_allow_html=True)

st.markdown("<br><hr style='border-color: #33000d;'>", unsafe_allow_html=True)

if st.button("TAKE ME NOW 🔥"):
    st.balloons()
    st.markdown("<h2 style='text-align: center; color: #ff0055;'>Good girl. Wait for me.</h2>", unsafe_allow_html=True)

import streamlit as st
from streamlit_lottie import st_lottie
import requests
from gtts import gTTS
import base64
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="Private Session", page_icon="🔞", layout="centered")

# --- UI & MUSIC SETUP ---
def add_bg_music():
    # A slow, rhythmic Bollywood-style instrumental/track
    # Setting volume to 0.1 so it stays very low in the background
    music_url = "https://www.pagalworld.com.sb/files/download/id/68172" # Instrumental Sample
    st.markdown(f"""
        <audio id="bg-music" autoplay loop inline>
            <source src="{music_url}" type="audio/mp3">
        </audio>
        <script>
            var audio = document.getElementById("bg-music");
            audio.volume = 0.1; 
        </script>
        """, unsafe_allow_html=True)

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #120101, #2b0000, #000000); }
    .stButton>button {
        background: linear-gradient(45deg, #d00000, #3a0000);
        color: white;
        border-radius: 12px;
        height: 4em;
        width: 100%;
        border: 1px solid #ff4d4d;
        font-weight: bold;
        font-size: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
    }
    .stButton>button:hover {
        box-shadow: 0px 0px 15px #ff0000;
        border: 1px solid #ffffff;
        color: #ffcccc;
    }
    .message-box {
        background: rgba(40, 0, 0, 0.7);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #ff0000;
        text-align: center;
        color: #ff9999;
        font-size: 20px;
        margin-bottom: 20px;
        font-family: 'Courier New', Courier, monospace;
    }
    h1 { text-shadow: 0px 0px 15px #ff0000; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

def play_audio(text, lang):
    try:
        # Using specific locales for deeper/more masculine 'male-ish' tones
        tts = gTTS(text=text, lang=lang, slow=False)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        audio_b64 = base64.b64encode(fp.read()).decode()
        # Voice is played at full volume (default) while music is at 0.1
        audio_tag = f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_b64}">'
        st.markdown(audio_tag, unsafe_allow_html=True)
    except: st.error("Voice Error")

# --- APP START ---
add_bg_music()
st.markdown("<h1 style='text-align: center;'>🥵 Dark Whispers</h1>", unsafe_allow_html=True)

# --- THE RHYMES ---
msg_data = {
    "English 🇬🇧": ("Harder, deeper, do it again... I'm your master, not your friend. Under the sheets, lose control... I’m gonna take your very soul.", "en-uk"),
    "Hindi 🇮🇳": ("Raat akeli, badan hai garm... Tod do saari sharam o marm. Upar niche, mere saath... Thamlo kas ke mera haath.", "hi"),
    "Urdu 🇵🇰": ("Be-sharm nigaahein, garm saansein... Aaj poori hongi sab muraadein. Kapre utaaro, paas aao... Mujhe apni tapan dikhao.", "ur"),
    "Telugu 🇮🇳": ("Nee vedi naa paina, naa cheyi nee lona... ee raatri manadi, telusa maina? Paiki kindaki, ninnu laaguta... nee tapanani nenu teerusta.", "te"),
    "Spanish 🇪🇸": ("Pégate a mí, siente el calor... Te voy a dar mucho dolor y amor. Contra la pared, sin ropa ya... Mi cuerpo en el tuyo se quedará.", "es"),
    "Chinese 🇨🇳": ("Bǎ yīfú tuōguāng, kào jìn wǒ... Wǒ yào kàn nǐ wèi wǒ zhuóhuǒ. Shàng xià lánshān, bùyào tíng... Nǐ de jiàochuán, wǒ de mìng.", "zh-cn"),
    "Korean 🇰🇷": ("Nae gyeoteuro wa, momeul matgyeo... Neo-ui han sum-eul naega gajyeo. Wi araero, deo sege... Oneul bam neon nae kkeoya.", "ko"),
    "Afghani (Dari)": ("Bia pesham, naza nako... Badanat ra garm o taza nako. Bala o payin, dar khedmat... Mekonum emshab, ba lezat.", "hi") # Using Hindi engine for similar phonetics
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

# --- MESSAGE BOX ---
if 'msg' in st.session_state:
    st.markdown(f'<div class="message-box">{st.session_state["msg"]}</div>', unsafe_allow_html=True)

st.markdown("<br><hr style='border-color: #550000;'>", unsafe_allow_html=True)

if st.button("MAKE ME MOAN 💦"):
    st.snow()
    st.write("<h3 style='text-align: center; color: white;'>Lock the door. I'm almost there.</h3>", unsafe_allow_html=True)

import streamlit as st
from streamlit_lottie import st_lottie
import requests
from gtts import gTTS
import base64
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="For My Bbygirl", page_icon="🔞", layout="centered")

# --- CUSTOM ROMANTIC CSS ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(to bottom, #ffafbd, #ffc3a0); }
    .stButton>button {
        background-color: #d63384;
        color: white;
        border-radius: 50px;
        height: 3em;
        width: 100%;
        border: 2px solid #ffffff;
        font-weight: bold;
        font-size: 18px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff4d6d;
        transform: scale(1.05);
    }
    .message-box {
        background-color: rgba(255, 255, 255, 0.2);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid white;
        text-align: center;
        color: white;
        font-size: 20px;
        margin-bottom: 20px;
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

# --- APP LAYOUT ---
lottie_main = get_lottie("https://lottie.host/8040409a-6756-4299-9759-33b68051a029/9f7l8fX7y9.json")
if lottie_main:
    st_lottie(lottie_main, height=300, key="main")

st.markdown("<h2 style='text-align: center; color: white;'>Press a button to hear me...</h2>", unsafe_allow_html=True)

# --- LANGUAGE DATA ---
msg_data = {
    "Sanskrit 🕉️": {"txt": "प्रिये, किं भवती मां खादितुं, दंष्टुं, आलिङ्गितुं, मैथुनं कर्तुं, लेढुं च इच्छति? मम वैलेंटाइन भव।", "code": "hi"},
    "Hindi 🇮🇳": {"txt": "बेबी गर्ल, क्या तुम मुझे खाना, काटना, गले लगाना, मेरे साथ हमबिस्तर होना और चाटना चाहती हो? मेरी वैलेंटाइन बन जाओ।", "code": "hi"},
    "Telugu 🇮🇳": {"txt": "బేబీ గర్ల్, నువ్వు నన్ను తినాలనుకుంటున్నావా, కరవాలనుకుంటున్నావా, కౌగిలించుకోవాలనుకుంటున్నావా, నాతో కలవాలనుకుంటున్నావా, నాకాలనుకుంటున్నావా? నా వాలెంటైన్ అవుతావా?", "code": "te"},
    "German 🇩🇪": {"txt": "Bbygirl, willst du mich essen, mich beißen, mich umarmen, mich ficken, mich lecken? Und sei mein Valentin.", "code": "de"},
    "Spanish 🇪🇸": {"txt": "Bbygirl, ¿quieres comerme, morderme, abrazarme, follarme, lamerme? Y sé mi Valentín.", "code": "es"},
    "Turkish 🇹🇷": {"txt": "Bbygirl, beni yemek mi, ısırmak mı, sarılmak mı, sikmek mi, yalamak mı istiyorsun? Ve sevgilim ol.", "code": "tr"},
    "French 🇫🇷": {"txt": "Bbygirl, tu veux me manger, me mordre, me câliner, me baiser, me lécher ? Et sois ma valentine.", "code": "fr"},
    "Korean 🇰🇷": {"txt": "Bbygirl, 나를 먹고 싶니, 깨물고 싶니, 안고 싶니, 나랑 섹스하고 싶니, 핥고 싶니? 그리고 나의 발렌타인이 되어줘.", "code": "ko"},
    "English 🇬🇧": {"txt": "Bbygirl do you wanna eat me bite me hug me fuck me lick me? And be my valentine.", "code": "en"},
    "Chinese 🇨🇳": {"txt": "Bbygirl, 你想吃我，咬我，抱我，跟我做爱，舔我吗？做我的情人吧。", "code": "zh-cn"},
    "Italian 🇮🇹": {"txt": "Bbygirl, vuoi mangiarmi, mordermi, abbracciarmi, scoparmi, leccarmi? E sii il mio Valentino.", "code": "it"}
}

# --- BUTTON GRID ---
cols = st.columns(2)
for i, (name, info) in enumerate(msg_data.items()):
    with cols[i % 2]:
        if st.button(name):
            # Display text on screen
            st.markdown(f'<div class="message-box">{info["txt"]}</div>', unsafe_allow_html=True)
            # Play audio
            play_audio(info['txt'], info['code'])

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

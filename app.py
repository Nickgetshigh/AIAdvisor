import streamlit as st
from streamlit_lottie import st_lottie
import requests
from gtts import gTTS
import base64
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="Global Love", page_icon="💖", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(to right, #ff9a9e 0%, #fecfef 100%); }
    .main-text {
        background-color: rgba(255, 255, 255, 0.4);
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #ff4d6d;
        color: #d63384;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #ff4d6d;
        color: white;
        border-radius: 12px;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #c9184a;
        transform: translateY(-2px);
    }
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
    except: pass

# --- APP ASSETS ---
lottie_main = get_lottie("https://lottie.host/8040409a-6756-4299-9759-33b68051a029/9f7l8fX7y9.json")
if lottie_main:
    st_lottie(lottie_main, height=200, key="main")

# --- LANGUAGE DATA ---
msg_data = {
    "Sanskrit 🕉️": {"txt": "प्रिये, किं भवती मां दंष्टुं, आलिङ्गितुं, मैथुनं कर्तुं, लेढुं च इच्छति? मम वैलेंटाइन भव।", "code": "hi"},
    "Hindi 🇮🇳": {"txt": "बेबी गर्ल, क्या तुम मुझे काटना, गले लगाना, मेरे साथ हमबिस्तर होना और चाटना चाहती हो? मेरी वैलेंटाइन बन जाओ।", "code": "hi"},
    "Telugu 🇮🇳": {"txt": "బేబీ గర్ల్, నువ్వు నన్ను తినాలనుకుంటున్నావా, కరవాలనుకుంటున్నావా, హత్తుకోవాలనుకుంటున్నావా, నాతో కలవాలనుకుంటున్నావా మరియు నాకాలనుకుంటున్నావా? నా వాలెంటైన్ అవుతావా.", "code": "te"},
    "Tamil 🇮🇳": {"txt": "பேபி கேர்ள், நீ என்னை சாப்பிட, கடிக்க, கட்டிப்பிடிக்க, என்னுடன் உறவு கொள்ள மற்றும் நக்க விரும்புகிறாயா? என் காதலியாக இரு.", "code": "ta"},
    "Kannada 🇮🇳": {"txt": "ಬೇಬಿ ಗರ್ಲ್, ನೀನು ನನ್ನನ್ನು ತಿನ್ನಲು, ಕಚ್ಚಲು, ಅಪ್ಪಿಕೊಳ್ಳಲು, ನನ್ನೊಂದಿಗೆ ಸಂಭೋಗಿಸಲು ಮತ್ತು ನೆಕ್ಕಲು ಬಯಸುವಿರಾ? ನನ್ನ ವ್ಯಾಲೆಂಟೈನ್ ಆಗು.", "code": "kn"},
    "Malayalam 🇮🇳": {"txt": "ബേബി ഗേൾ, നിനക്ക് എന്നെ കഴിക്കണോ, കടിക്കണോ, കെട്ടിപ്പിടിക്കണോ, എന്നോടൊപ്പം ശയിക്കണോ, നക്കണോ? എന്റെ വാലന്റൈൻ ആകുക.", "code": "ml"},
    "English 🇬🇧": {"txt": "Bbygirl, do you wanna eat me, bite me, hug me, fuck me, lick me? And be my valentine.", "code": "en"},
    "Chinese 🇨🇳": {"txt": "Bbygirl, 你想吃我，咬我，抱我，跟我做爱，舔我吗？做我的情人吧。", "code": "zh-cn"},
    "Korean 🇰🇷": {"txt": "Bbygirl, 나를 먹고 싶니, 깨물고 싶니, 안고 싶니, 나랑 섹스하고 싶니, 핥고 싶니? 그리고 나의 발렌타인이 되어줘.", "code": "ko"},
    "French 🇫🇷": {"txt": "Bbygirl, tu veux me manger, me mordre, me câliner, me baiser, me lécher ? Et sois ma valentine.", "code": "fr"},
    "German 🇩🇪": {"txt": "Bbygirl, willst du mich essen, mich beißen, mich umarmen, mich ficken, mich lecken? Und sei mein Valentin.", "code": "de"},
    "Spanish 🇪🇸": {"txt": "Bebé, ¿quieres comerme, morderme, abrazarme, follarme, lamerme? Y sé mi Valentín.", "code": "es"},
    "Turkish 🇹🇷": {"txt": "Bebeğim, beni yemek mi, ısırmak mı, sarılmak mı, sikmek mi, yalamak mı istiyorsun? Ve sevgilim ol.", "code": "tr"},
    "Italian 🇮🇹": {"txt": "Bbygirl, vuoi mangiarmi, mordermi, abbracciarmi, scoparmi, leccarmi? E sii il mio Valentino.", "code": "it"}
}

# Initialize choice
if 'current_text' not in st.session_state:
    st.session_state.current_text = "Select a language to see and hear the message..."

# Display Content Box
st.markdown(f'<div class="main-text">{st.session_state.current_text}</div>', unsafe_allow_html=True)

# Button Grid (2 columns for desktop, looks good on mobile too)
cols = st.columns(2)
for i, (name, info) in enumerate(msg_data.items()):
    with cols[i % 2]:
        if st.button(name, use_container_width=True):
            st.session_state.current_text = info['txt']
            play_audio(info['txt'], info['code'])
            st.rerun()

st.markdown("<br><hr>", unsafe_allow_html=True)

# Final Acceptance
c1, c2 = st.columns(2)
with c1:
    if st.button("YES! 😍", key="yes_btn"):
        st.balloons()
        st.success("Best Valentine's Day Ever!")
        lottie_celeb = get_lottie("https://lottie.host/67702580-f00a-42fb-a7e8-e4b779a5e8c1/m8n8C0zE9Y.json")
        if lottie_celeb: st_lottie(lottie_celeb, height=150)

with c2:
    if st.button("No 🥺", key="no_btn"):
        st.error("Access Denied: You belong to me! 😉")

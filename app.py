import streamlit as st
from streamlit_lottie import st_lottie
import requests

# --- PAGE CONFIG ---
st.set_page_config(page_title="For My Bbygirl", page_icon="🔞", layout="centered")

# --- CSS ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(to bottom, #2c003e, #fe2851); }
    .stButton>button {
        background-color: #ff0055; color: white; border-radius: 15px;
        height: 4em; width: 100%; border: none; font-weight: bold;
    }
    .message-box {
        background: rgba(0, 0, 0, 0.5); padding: 20px; border-radius: 15px;
        text-align: center; color: white; font-style: italic; margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- JAVASCRIPT VOICE ENGINE ---
def local_speak(text, lang_code):
    # This JS finds a male voice and speaks
    js_code = f"""
        <script>
        var msg = new SpeechSynthesisUtterance();
        msg.text = "{text}";
        msg.lang = "{lang_code}";
        
        // Try to find a male voice
        var voices = window.speechSynthesis.getVoices();
        var maleVoice = voices.find(voice => voice.name.includes('Male') || voice.name.includes('David') || voice.name.includes('Google UK English Male'));
        
        if (maleVoice) {{
            msg.voice = maleVoice;
        }}
        msg.pitch = 0.8; // Lower pitch for sexier tone
        msg.rate = 0.9;  // Slightly slower
        window.speechSynthesis.speak(msg);
        </script>
    """
    st.components.v1.html(js_code, height=0)

# --- APP LAYOUT ---
st.markdown("<h2 style='text-align: center; color: white;'>Touch a language to hear me...</h2>", unsafe_allow_html=True)

lyric_txt = "So you want me, and you need me... Come bby to me, right now, now, now. Bbygirl I'll take you up and down, Spinning your heart round and round."

msg_data = {
    "English 🇬🇧": {"txt": lyric_txt, "code": "en-US"},
    "Telugu 🇮🇳": {"txt": "నీకు నేను కావాలి, నీకు నా అవసరం ఉంది. ఇప్పుడే నా దగ్గరకు రా. నిన్ను పైకి కిందకి తీసుకెళ్తా, లోకాన్ని చుట్టూ తిప్పుతా.", "code": "te-IN"},
    "Hindi 🇮🇳": {"txt": "तुम्हें मेरी चाहत है, तुम्हें मेरी ज़रूरत है. अभी मेरे पास आओ. मैं तुम्हें ऊपर-नीचे ले जाऊंगा, और गोल-गोल घुमाऊंगा।", "code": "hi-IN"},
    "Spanish 🇪🇸": {"txt": "Me quieres y me necesitas. Ven a mí ahora mismo. Te llevaré de arriba abajo, dándote vueltas una y otra vez.", "code": "es-ES"}
}

cols = st.columns(2)
for i, (name, info) in enumerate(msg_data.items()):
    with cols[i % 2]:
        if st.button(name):
            st.markdown(f'<div class="message-box">{info["txt"]}</div>', unsafe_allow_html=True)
            local_speak(info['txt'], info['code'])

if st.button("YES! 😍"):
    st.balloons()
    st.markdown("<h3 style='text-align: center; color: white;'>You're mine. ❤️</h3>", unsafe_allow_html=True)

import streamlit as st
from streamlit_lottie import st_lottie
import requests
from gtts import gTTS
import base64
import io

# --- CONFIG ---
st.set_page_config(page_title="For My Love", page_icon="❤️")

def get_lottie(url):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

def play_audio(text, lang):
    tts = gTTS(text=text, lang=lang)
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    audio_b64 = base64.b64encode(fp.read()).decode()
    audio_tag = f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_b64}">'
    st.markdown(audio_tag, unsafe_allow_html=True)

# --- ASSETS ---
lottie_hearts = get_lottie("https://assets5.lottiefiles.com/packages/lf20_028fb997.json")

# --- UI ---
st_lottie(lottie_hearts, height=200)

if 'language' not in st.session_state:
    st.session_state.language = 'Chinese'

col1, col2 = st.columns([2, 1])

with col1:
    if st.session_state.language == 'Chinese':
        st.title("你会做我的情人吗？")
        msg = "你会做我的情人吗？"
        lang_code = 'zh-cn'
        btn_text = "Translate to Hindi 🇮🇳"
    else:
        st.title("क्या तुम मेरी वैलेंटाइन बनोगी?")
        msg = "क्या तुम मेरी वैलेंटाइन बनोगी?"
        lang_code = 'hi'
        btn_text = "Translate to Chinese 🇨🇳"

# --- TRANSLATION LOGIC ---
if st.button(btn_text):
    st.session_state.language = 'Hindi' if st.session_state.language == 'Chinese' else 'Chinese'
    st.rerun()

# --- AUDIO AUTOPLAY ---
play_audio(msg, lang_code)

# --- THE RESPONSE ---
if st.button("YES! ❤️"):
    st.balloons()
    st.success("I love you! Forever and always.")
    st_lottie(get_lottie("https://assets.lottiefiles.com/packages/lf20_icu196n1.json"))

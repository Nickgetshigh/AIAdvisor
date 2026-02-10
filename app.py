import streamlit as st
import time
import random

st.set_page_config(page_title="💔 10-SEC HEART CHASE 💔", page_icon="❤️", layout="wide")

# Initialize session state
if 'game_state' not in st.session_state:
    st.session_state.game_state = 'start'
if 'start_time' not in st.session_state:
    st.session_state.start_time = 0
if 'time_left' not in st.session_state:
    st.session_state.time_left = 10
if 'heart_x' not in st.session_state:
    st.session_state.heart_x = 50
if 'heart_y' not in st.session_state:
    st.session_state.heart_y = 50

# FIXED CSS - NO SCROLL
st.markdown("""
<style>
html, body { margin: 0; padding: 0; overflow: hidden; height: 100vh; }
.main { padding: 0 !important; background: linear-gradient(135deg, #ff1744, #ff6b9d) !important; height: 100vh !important; }
.game-frame { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; overflow: hidden; background: radial-gradient(circle, #ff69b4 0%, #ff1493 70%); }
.heart-clickable { position: absolute; font-size: 80px; cursor: pointer; z-index: 9999; text-shadow: 0 0 25px #fff, 0 0 35px #ff1493; transition: all 0.1s ease; animation: heartbeat 0.4s infinite; }
@keyframes heartbeat { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.2); } }
.stats { position: fixed; top: 15px; left: 15px; right: 15px; background: rgba(0,0,0,0.8); color: #ffd700; padding: 12px; border-radius: 15px; font-size: 22px; font-weight: bold; text-align: center; z-index: 10000; }
.lose-screen { position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background: rgba(0,0,0,0.95); color: #ff1493; padding: 40px; border-radius: 25px; text-align: center; font-size: 32px; border: 3px solid gold; z-index: 10001; }
.restart-btn { position: fixed; bottom: 25px; right: 25px; background: linear-gradient(45deg, gold, orange); color: black; padding: 15px 30px; border: none; border-radius: 50px; font-size: 20px; font-weight: bold; cursor: pointer; box-shadow: 0 8px 25px rgba(255,165,0,0.6); }
</style>
""", unsafe_allow_html=True)

if st.session_state.game_state == 'start':
    st.markdown('<div class="game-frame">', unsafe_allow_html=True)
    
    # START SCREEN
    st.markdown("""
    <div style='position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 48px; color: gold; text-align: center; text-shadow: 0 0 30px #ff1493; z-index: 10002;'>
        💖 **10 SECONDS TO CATCH THE HEART!** 💖<br>
        <span style='font-size: 24px; color: white;'>Click the moving heart exactly!</span>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 **START CHASE** 🚀", key="start_btn", use_container_width=True):
        st.session_state.game_state = 'playing'
        st.session_state.start_time = time.time()
        st.session_state.time_left = 10
        st.session_state.heart_x = random.randint(10, 90)
        st.session_state.heart_y = random.randint(10, 90)
        st.rerun()
        
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.game_state == 'playing':
    # TIMER
    elapsed = time.time() - st.session_state.start_time
    st.session_state.time_left = max(0, 10 - elapsed)
    
    st.markdown('<div class="game-frame">', unsafe_allow_html=True)
    
    # LIVE TIMER
    st.markdown(f"""
    <div class="stats">
        ⏰ **{st.session_state.time_left:.1f}s LEFT** ⏰
    </div>
    """, unsafe_allow_html=True)
    
    # CLICKABLE HEART
    heart_style = f"""
    <div class="heart-clickable" 
         style="left: {st.session_state.heart_x}%; top: {st.session_state.heart_y}%;
         transition-duration: 0.05s;" 
         onclick="document.querySelector('#heart_click_trigger').click()">
        💖
    </div>
    """
    st.markdown(heart_style, unsafe_allow_html=True)
    
    # HEART CLICK DETECTOR
    if st.button(" ", key="heart_click_trigger"):
        # ULTRA FAST JUMP TO NEW POSITION
        st.session_state.heart_x = random.randint(5, 95)
        st.session_state.heart_y = random.randint(5, 95)
        st.success("💥 HEART JUMPED! Keep trying!")
        st.balloons()
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # LOSER SCREEN
    if st.session_state.time_left <= 0:
        st.session_state.game_state = 'lost'
        st.markdown("""
        <div class="lose-screen">
            💔 **LOSER! TIME UP!** 💔<br><br>
            <span style='color: gold; font-size: 28px;'>Heart escaped your clumsy fingers! 😭</span>
        </div>
        """, unsafe_allow_html=True)
        st.rerun()

# RESTART BUTTON
st.markdown("""
<div class="restart-btn" onclick="window.location.reload()">
    🔄 **NEW GAME**
</div>
""", unsafe_allow_html=True)

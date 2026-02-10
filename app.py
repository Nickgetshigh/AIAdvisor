import streamlit as st
import time
import random

st.set_page_config(page_title="💔 10-SEC HEART CHASE 💔", page_icon="❤️", layout="wide")

# Initialize
if 'game_state' not in st.session_state: st.session_state.game_state = 'start'
if 'start_time' not in st.session_state: st.session_state.start_time = 0
if 'time_left' not in st.session_state: st.session_state.time_left = 10
if 'heart_x' not in st.session_state: st.session_state.heart_x = 50
if 'heart_y' not in st.session_state: st.session_state.heart_y = 50
if 'clicks' not in st.session_state: st.session_state.clicks = 0

# FIXED FRAME CSS
st.markdown("""
<style>
html, body { margin: 0; padding: 0; overflow: hidden; height: 100vh; }
.main { padding: 0 !important; background: linear-gradient(135deg, #ff1744, #ff6b9d) !important; height: 100vh !important; }
.game-frame { 
    position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; 
    overflow: hidden; background: radial-gradient(circle, #ff69b4 0%, #ff1493 70%);
}
.heart-target {
    position: absolute; width: 100px; height: 100px; 
    cursor: pointer; z-index: 9999; border-radius: 50%;
    background: radial-gradient(circle, rgba(255,20,147,0.8), transparent);
    transition: all 0.1s ease;
}
.heart-target:hover {
    transform: scale(1.4) !important; box-shadow: 0 0 40px #ff1493;
}
.heart-glow {
    position: absolute; font-size: 70px; 
    pointer-events: none; text-shadow: 0 0 30px #fff;
    animation: heartbeat 0.5s infinite;
}
@keyframes heartbeat {
    0%, 100% { transform: scale(1); } 50% { transform: scale(1.2); }
}
.stats { 
    position: fixed; top: 15px; left: 15px; right: 15px; 
    background: rgba(0,0,0,0.85); color: #ffd700; padding: 15px; 
    border-radius: 20px; font-size: 24px; font-weight: bold; text-align: center; z-index: 10000; 
}
.lose-screen { 
    position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); 
    background: rgba(0,0,0,0.95); color: #ff1493; padding: 50px; 
    border-radius: 30px; text-align: center; font-size: 36px; 
    border: 4px solid gold; z-index: 10001; box-shadow: 0 0 50px #ff1493;
}
</style>
""", unsafe_allow_html=True)

if st.session_state.game_state == 'start':
    st.markdown('<div class="game-frame">', unsafe_allow_html=True)
    
    st.markdown("""
    <div style='position: fixed; top: 45%; left: 50%; transform: translate(-50%, -50%); 
        font-size: 50px; color: gold; text-align: center; text-shadow: 0 0 40px #ff1493; z-index: 10002;'>
        💖 **CATCH THE HEART IN 10 SECONDS!** 💖<br>
        <span style='font-size: 28px; color: white;'>Click the glowing heart circle!</span>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 **START GAME** 🚀", key="start"):
        st.session_state.game_state = 'playing'
        st.session_state.start_time = time.time()
        st.session_state.time_left = 10
        st.session_state.clicks = 0
        st.session_state.heart_x = random.randint(15, 85)
        st.session_state.heart_y = random.randint(15, 85)
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.game_state == 'playing':
    elapsed = time.time() - st.session_state.start_time
    st.session_state.time_left = max(0, 10 - elapsed)
    
    st.markdown('<div class="game-frame">', unsafe_allow_html=True)
    
    # STATS
    st.markdown(f"""
    <div class="stats">
        ⏰ **{st.session_state.time_left:.1f}s** | 💥 **{st.session_state.clicks} clicks** 
    </div>
    """, unsafe_allow_html=True)
    
    # HEART TARGET ZONE (PERFECTLY OVER HEART)
    heart_style = f"""
    <div class="heart-target" 
         style="left: {st.session_state.heart_x}%; top: {st.session_state.heart_y}%;
         transform: translate(-50%, -50%);"
         title="Click me!">
    </div>
    <div class="heart-glow" 
         style="left: {st.session_state.heart_x}%; top: {st.session_state.heart_y}%;
         transform: translate(-50%, -50%);">
        💖
    </div>
    """
    st.markdown(heart_style, unsafe_allow_html=True)
    
    # MICRO CLICK BUTTON (INSIDE TARGET ZONE)
    col1, col2 = st.columns([3,1])
    with col2:
        if st.button("💖", key="heart_hit", help=""):
            st.session_state.clicks += 1
            st.session_state.heart_x = random.randint(5, 95)
            st.session_state.heart_y = random.randint(5, 95)
            st.balloons()
            st.success("💥 HEART JUMPED!")
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.session_state.time_left <= 0:
        st.session_state.game_state = 'lost'
        st.markdown("""
        <div class="lose-screen">
            💔 **LOSER! TIME UP!** 💔<br><br>
            <span style='color: gold; font-size: 32px;'>Heart outsmarted you! {st.session_state.clicks} clicks</span>
        </div>
        """, unsafe_allow_html=True)
        st.rerun()

# RESTART
st.markdown("""
<div onclick="window.location.reload()" style='
    position: fixed; bottom: 20px; right: 20px; z-index: 10002;
    background: linear-gradient(45deg, gold, #ff6b9d); color: black; 
    padding: 20px 35px; border: none; border-radius: 50px; 
    font-size: 22px; font-weight: bold; cursor: pointer; 
    box-shadow: 0 10px 30px rgba(255,20,147,0.6);'>
    🔄 NEW GAME
</div>
""", unsafe_allow_html=True)

import streamlit as st
import time
import random

st.set_page_config(page_title="🌺 Jalebi Swirl Challenge 🌺", page_icon="🧡", layout="wide")

# MOBILE-FRIENDLY DESI CSS - HIDE STREAMLIT UI
st.markdown("""
<style>
html, body { 
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
    background: linear-gradient(135deg, #ff6b35, #f7931e, #ffcc02) !important;
    margin: 0 !important; padding: 0 !important; overflow-x: hidden !important;
}
.main { 
    max-width: 420px !important; margin: 0 auto !important; padding: 1rem !important;
    background: rgba(255,255,255,0.95) !important; border-radius: 25px !important;
    box-shadow: 0 20px 60px rgba(255,107,53,0.4) !important;
}
header, footer { display: none !important; }
.stButton > button { 
    width: 100% !important; height: 70px !important; 
    background: linear-gradient(45deg, #ff6b35, #f7931e) !important;
    color: white !important; font-size: 22px !important; font-weight: bold !important;
    border-radius: 20px !important; border: none !important; margin: 10px 0 !important;
    box-shadow: 0 10px 30px rgba(255,107,53,0.4) !important;
}
.jalebi-frame {
    position: relative; height: 400px; background: 
    radial-gradient(circle at 30% 30%, #ffcc02 0%, transparent 50%),
    radial-gradient(circle at 70% 70%, #ff6b35 0%, transparent 50%);
    border-radius: 20px; overflow: hidden; margin: 20px 0;
}
.jalebi {
    position: absolute; font-size: 90px; cursor: pointer; 
    transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    text-shadow: 0 0 20px #ffcc02;
}
.jalebi:hover { transform: scale(1.3) !important; animation: wiggle 0.2s !important; }
@keyframes wiggle {
    0%, 100% { transform: rotate(0deg) scale(1.3); }
    25% { transform: rotate(5deg) scale(1.35); }
    75% { transform: rotate(-5deg) scale(1.35); }
}
.stats-bar {
    background: linear-gradient(90deg, #ff6b35, #f7931e); color: white;
    padding: 15px; border-radius: 15px; text-align: center; font-size: 20px;
    font-weight: bold; margin: 10px 0;
}
.glitch { animation: glitch 0.3s infinite !important; color: #ff1744 !important; }
@keyframes glitch {
    0%, 100% { transform: translate(0); }
    20% { transform: translate(-2px, 2px); }
    40% { transform: translate(-2px, -2px); }
    60% { transform: translate(2px, 2px); }
    80% { transform: translate(2px, -2px); }
}
.penalty-card {
    background: linear-gradient(135deg, #ff6b35, #f7931e); color: white;
    padding: 30px; border-radius: 25px; text-align: center; margin: 20px 0;
    box-shadow: 0 15px 40px rgba(255,107,53,0.5); border: 3px solid #ffcc02;
}
</style>
""", unsafe_allow_html=True)

# SESSION STATE
if 'game_state' not in st.session_state: st.session_state.game_state = 'start'
if 'start_time' not in st.session_state: st.session_state.start_time = 0
if 'clicks' not in st.session_state: st.session_state.clicks = 0
if 'jalebi_x' not in st.session_state: st.session_state.jalebi_x = 50
if 'jalebi_y' not in st.session_state: st.session_state.jalebi_y = 50

def new_jalebi_position():
    st.session_state.jalebi_x = random.randint(15, 85)
    st.session_state.jalebi_y = random.randint(15, 85)

if st.session_state.game_state == 'start':
    st.markdown("## 🌺 **JALEBI SWIRL CHALLENGE** 🌺")
    st.markdown("**Catch 3 swirling jalebis in 10 seconds! 🍬💕**")
    
    if st.button("🧡 **START SWEET CHASE** 🧡"):
        st.session_state.game_state = 'playing'
        st.session_state.start_time = time.time()
        st.session_state.clicks = 0
        new_jalebi_position()
        st.rerun()

elif st.session_state.game_state == 'playing':
    elapsed = time.time() - st.session_state.start_time
    time_left = max(0, 10 - elapsed)
    
    # STATS
    st.markdown(f"""
    <div class="stats-bar">
        ⏰ **{time_left:.1f}s** | 🧡 **{st.session_state.clicks}/3 Jalebis** 
    </div>
    """, unsafe_allow_html=True)
    
    # JALEBI FRAME
    st.markdown('<div class="jalebi-frame">', unsafe_allow_html=True)
    
    # MOVING JALEBI
    jalebi_style = f"""
    <div class="jalebi" 
         style="left: {st.session_state.jalebi_x}%; top: {st.session_state.jalebi_y}%;
         transform: translate(-50%, -50%);">
        🧿
    </div>
    """
    st.markdown(jalebi_style, unsafe_allow_html=True)
    
    # CLICK ZONE (OVER JALEBI)
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("🍬", key="jalebi_click"):
            st.session_state.clicks += 1
            st.balloons()
            new_jalebi_position()
            if st.session_state.clicks >= 3 or time_left <= 0:
                st.session_state.game_state = 'glitch'
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # CHECK GAME OVER
    if st.session_state.clicks >= 3 or time_left <= 0:
        st.session_state.game_state = 'glitch'
        st.rerun()

elif st.session_state.game_state == 'glitch':
    st.markdown("""
    <div style='text-align: center; padding: 40px;'>
        <h1 class="glitch">🚨 ERROR: SWEETNESS OVERLOAD! 🚨</h1>
        <h2 class="glitch">**SYSTEM CRASH** 💥🍬</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="penalty-card">
        <h2>😭 **DEFEAT! Jalebis escaped!** 😭</h2>
        <div style='font-size: 28px; margin: 20px 0;'>🛍️ **PENALTY TIME** 🛍️</div>
        <div style='font-size: 24px; background: rgba(255,255,255,0.2); padding: 20px; border-radius: 15px;'>
            **As per the Laws of Love**<br>
            <span style='color: #ffcc02; font-size: 26px; font-weight: bold;'>[YOUR NAME]</span><br>
            **must receive a NEW KURTA or HOODIE!** 🎉
        </div>
        <div style='font-size: 20px; margin-top: 20px; opacity: 0.9;'>
            📸 **Screenshot this and send to claim your prize!** 📸
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔄 **NEW CHALLENGE** 🔄"):
        for key in list(st.session_state.keys()):
            if key != 'game_state':
                del st.session_state[key]
        st.session_state.game_state = 'start'
        st.rerun()

# FOOTER LOVE MESSAGE
st.markdown("""
<div style='text-align: center; margin-top: 30px; color: #ff6b35; font-size: 18px;'>
    💕 Made with Desi Love for Valentine's Day 💕
</div>
""", unsafe_allow_html=True)

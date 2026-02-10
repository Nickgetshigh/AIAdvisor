import streamlit as st
import time
import random
import math

st.set_page_config(page_title="💔 FAST HEART CHASE 💔", page_icon="❤️", layout="wide")

# Initialize
if 'game_state' not in st.session_state: st.session_state.game_state = 'playing'
if 'start_time' not in st.session_state: st.session_state.start_time = time.time()
if 'time_left' not in st.session_state: st.session_state.time_left = 30
if 'angle' not in st.session_state: st.session_state.angle = 0
if 'speed' not in st.session_state: st.session_state.speed = 0.4  # HIGH SPEED!
if 'center_x' not in st.session_state: st.session_state.center_x = 50
if 'center_y' not in st.session_state: st.session_state.center_y = 50
if 'radius' not in st.session_state: st.session_state.radius = 35
if 'click_count' not in st.session_state: st.session_state.click_count = 0

# FIXED FRAME - NO SCROLL CSS
st.markdown("""
<style>
html, body {
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden !important;
}
.main {
    padding: 0 !important;
    background: linear-gradient(135deg, #ff1744, #ff6b9d, #ff9ff3) !important;
    margin: 0 !important;
}
.game-frame {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
    overflow: hidden !important;
    background: radial-gradient(circle, #ff69b4 0%, #ff1493 100%);
}
.heart-orbit {
    position: absolute !important;
    font-size: 90px !important;
    pointer-events: none !important;
    z-index: 9999 !important;
    text-shadow: 0 0 30px #fff, 0 0 40px #ff1493 !important;
    filter: drop-shadow(0 0 20px #ff1493);
}
@keyframes superpulse {
    0% { transform: scale(1) rotate(0deg); }
    25% { transform: scale(1.4) rotate(90deg); }
    50% { transform: scale(1.2) rotate(180deg); }
    75% { transform: scale(1.5) rotate(270deg); }
    100% { transform: scale(1) rotate(360deg); }
}
.click-trap {
    position: absolute !important;
    width: 100vw !important;
    height: 100vh !important;
    opacity: 0 !important;
    z-index: 10000 !important;
}
.stats {
    position: fixed !important;
    top: 10px !important;
    left: 10px !important;
    background: rgba(0,0,0,0.7) !important;
    color: gold !important;
    padding: 15px !important;
    border-radius: 20px !important;
    font-size: 20px !important;
    font-weight: bold !important;
    z-index: 10001 !important;
}
</style>
""", unsafe_allow_html=True)

# START MESSAGE OVERLAY
if st.session_state.game_state == 'playing':
    elapsed = time.time() - st.session_state.start_time
    st.session_state.time_left = max(0, 30 - elapsed)
    st.session_state.angle += st.session_state.speed  # ULTRA FAST!
    
    # PERFECT CIRCULAR MOTION - NEVER SKIPS SCREEN
    heart_x = 50 + 35 * math.cos(st.session_state.angle)  # Fixed center 50,50
    heart_y = 50 + 35 * math.sin(st.session_state.angle)
    
    # FULL SCREEN FRAME
    st.markdown('<div class="game-frame">', unsafe_allow_html=True)
    
    # START MESSAGE (first 3 seconds)
    if elapsed < 3:
        st.markdown("""
        <div style='
            position: fixed; 
            top: 50%; left: 50%; 
            transform: translate(-50%, -50%);
            font-size: 48px; 
            color: gold; 
            text-shadow: 0 0 30px #ff1493;
            z-index: 10002;
            animation: glow 1s infinite;
        '>
            🏃‍♂️ **CATCH THE HEART!** 🏃‍♂️
        </div>
        <style>
        @keyframes glow { 0%, 100% { text-shadow: 0 0 20px gold; } 50% { text-shadow: 0 0 40px #ff1493; } }
        </style>
        """, unsafe_allow_html=True)
    
    # LIVE STATS
    st.markdown(f"""
    <div class="stats">
        ⏰ {st.session_state.time_left:.1f}s | 
        🖱️ {st.session_state.click_count} | 
        ⚡ {int(st.session_state.angle*180/math.pi)%360}°
    </div>
    """, unsafe_allow_html=True)
    
    # FAST REVOLVING HEART
    st.markdown(f"""
    <div class="heart-orbit" 
         style="left: {heart_x}%; top: {heart_y}%; animation: superpulse 0.3s infinite;">
        💖
    </div>
    """, unsafe_allow_html=True)
    
    # INVISIBLE FULLSCREEN CLICK DETECTOR
    if st.button("", key="click_trap", help=""):
        st.session_state.click_count += 1
        st.session_state.speed += 0.05  # GETS FASTER WITH CLICKS!
        st.info("💥 HEART SCARED! SPEED INCREASED!")
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # TIME UP
    if st.session_state.time_left <= 0:
        st.session_state.game_state = 'lost'
        st.rerun()

elif st.session_state.game_state == 'lost':
    st.markdown("""
    <div style='
        position: fixed; 
        top: 50%; left: 50%; 
        transform: translate(-50%, -50%);
        background: rgba(0,0,0,0.9);
        color: #ff1493;
        padding: 40px;
        border-radius: 25px;
        text-align: center;
        font-size: 28px;
        z-index: 10002;
    '>
        💔 **TIME UP!** 💔<br>
        <span style='color: gold; font-size: 36px;'>Final: {st.session_state.click_count} scares!</span>
    </div>
    """, unsafe_allow_html=True)

# RESTART (bottom corner)
st.markdown("""
<div style='
    position: fixed; 
    bottom: 20px; right: 20px; 
    z-index: 10003;
'>
    <button onclick="window.location.reload()" 
            style="
                background: linear-gradient(45deg, gold, #ff1493);
                color: black; 
                padding: 15px 25px; 
                border: none; 
                border-radius: 50px; 
                font-size: 20px; 
                font-weight: bold;
                cursor: pointer;
                box-shadow: 0 10px 30px rgba(255,20,147,0.5);
            ">
        🔄 NEW GAME
    </button>
</div>
""", unsafe_allow_html=True)

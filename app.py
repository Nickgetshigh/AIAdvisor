import streamlit as st
import time
import random
import math

st.set_page_config(page_title="💔 Revolving Heart Chase 💔", page_icon="❤️", layout="wide")

# Initialize session state
if 'game_state' not in st.session_state: st.session_state.game_state = 'start'
if 'start_time' not in st.session_state: st.session_state.start_time = 0
if 'time_left' not in st.session_state: st.session_state.time_left = 30
if 'center_x' not in st.session_state: st.session_state.center_x = 50
if 'center_y' not in st.session_state: st.session_state.center_y = 50
if 'radius' not in st.session_state: st.session_state.radius = 30
if 'angle' not in st.session_state: st.session_state.angle = 0
if 'speed' not in st.session_state: st.session_state.speed = 0.1
if 'click_count' not in st.session_state: st.session_state.click_count = 0
if 'last_click_time' not in st.session_state: st.session_state.last_click_time = 0

st.markdown("""
<style>
.main {background: linear-gradient(135deg, #ff6b9d, #c44569, #ff9ff3);}
.game-container {position: relative; height: 500px; background: rgba(0,0,0,0.1);}
.heart-orbit {
    position: absolute;
    font-size: 70px;
    pointer-events: none;
    z-index: 1000;
    text-shadow: 0 0 20px #ff1493;
    animation: pulse 0.6s infinite;
}
.click-zone {height: 100px; width: 100%; cursor: pointer;}
</style>
""", unsafe_allow_html=True)

## GAME STATES
if st.session_state.game_state == 'start':
    st.title("💕 **Revolving Heart Challenge** 💕")
    st.write("**NO BUTTONS!** Heart revolves automatically. **Click ANYWHERE on screen** to scare it away! 30 seconds total! 🏃‍♂️💨")
    
    if st.button("🎮 **START REVOLVING HEART** 🎮", use_container_width=True):
        st.session_state.game_state = 'playing'
        st.session_state.start_time = time.time()
        st.session_state.time_left = 30
        st.session_state.angle = 0
        st.session_state.click_count = 0
        st.session_state.last_click_time = 0
        st.rerun()

elif st.session_state.game_state == 'playing':
    # Update timer
    elapsed = time.time() - st.session_state.start_time
    st.session_state.time_left = max(0, 30 - elapsed)
    
    # Update angle for circular motion
    st.session_state.angle += st.session_state.speed
    
    # Calculate heart position (circular orbit)
    heart_x = st.session_state.center_x + st.session_state.radius * math.cos(st.session_state.angle)
    heart_y = st.session_state.center_y + st.session_state.radius * math.sin(st.session_state.angle)
    
    # Check for recent click (jumps to new orbit)
    current_time = time.time()
    if current_time - st.session_state.last_click_time < 0.5:
        # Jump to new random center after click
        st.session_state.center_x = random.randint(20, 80)
        st.session_state.center_y = random.randint(20, 80)
        st.session_state.radius = random.randint(25, 40)
        st.session_state.click_count += 1
    
    st.session_state.last_click_time = current_time
    
    # Header
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("⏰ Time", f"{st.session_state.time_left:.1f}s")
    with col2: st.metric("🖱️ Clicks", st.session_state.click_count)
    with col3: st.metric("💖 Orbit", f"{int(st.session_state.angle*180/math.pi)%360}°")
    
    # FULL SCREEN GAME ZONE - CLICK ANYWHERE!
    st.markdown('<div class="game-container">', unsafe_allow_html=True)
    
    # MOVING REVOLVING HEART (NON CLICKABLE)
    heart_style = f"""
    <div class="heart-orbit" 
         style="left: {heart_x}%; top: {heart_y}%;">
        💖
    </div>
    <style>
    @keyframes pulse {{
        0% {{ transform: scale(1); }}
        50% {{ transform: scale(1.3); }}
        100% {{ transform: scale(1); }}
    }}
    </style>
    """
    st.markdown(heart_style, unsafe_allow_html=True)
    
    # INVISIBLE FULLSCREEN CLICK ZONE (triggers on ANY click)
    if st.button("👆 **CLICK ANYWHERE TO SCARE HEART!** 👆", 
                 key="screen_click", help="Click here or anywhere!"):
        st.session_state.last_click_time = time.time()
        st.info("💥 HEART SCARED! New orbit! 🏃‍♂️")
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Time up
    if st.session_state.time_left <= 0:
        st.session_state.game_state = 'lost'
        st.rerun()

elif st.session_state.game_state == 'lost':
    st.markdown("## 💥 **TIME UP! Heart escaped forever!** 💥")
    st.metric("📊 Final Stats", f"{st.session_state.click_count} scares in 30s!")
    
    dares = [
        "💃 **Send a dancing selfie** to your crush!",
        "🍫 **Buy heart chocolates** (show receipt!)",
        "💌 **Write a love note** on paper!",
        "🎵 **Record love song cover** (30 sec!)",
        "🌹 **Draw a heart** and send photo!"
    ]
    
    dare_choice = st.radio("**Pick your Valentine Penalty Dare:**", dares)
    if st.button("✅ **I ACCEPT PENALTY!**", use_container_width=True):
        st.session_state.game_state = 'dare_selected'
        st.balloons()
        st.rerun()

elif st.session_state.game_state == 'dare_selected':
    st.success("✅ **Dare locked in! Complete your penalty! 💖**")

# ALWAYS SHOW RESTART
st.markdown("---")
if st.button("🔄 **NEW REVOLVING HEART**", use_container_width=True):
    for key in list(st.session_state.keys()):
        if key != 'game_state':
            del st.session_state[key]
    st.session_state.game_state = 'start'
    st.rerun()

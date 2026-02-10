import streamlit as st
import time
import random

st.set_page_config(page_title="💔 Chase the Moving Heart 💔", page_icon="❤️", layout="wide")

# Initialize session state
if 'game_state' not in st.session_state: st.session_state.game_state = 'start'
if 'start_time' not in st.session_state: st.session_state.start_time = 0
if 'time_left' not in st.session_state: st.session_state.time_left = 30
if 'heart_x' not in st.session_state: st.session_state.heart_x = 0
if 'heart_y' not in st.session_state: st.session_state.heart_y = 0
if 'direction_x' not in st.session_state: st.session_state.direction_x = 1
if 'direction_y' not in st.session_state: st.session_state.direction_y = 1

st.markdown("""
<style>
.main {background: linear-gradient(135deg, #ff6b9d, #c44569, #ff9ff3);}
body {overflow-x: hidden;}
.heart-display {font-size: 80px; position: relative;}
.game-zone {height: 400px; background: rgba(255,255,255,0.1);}
</style>
""", unsafe_allow_html=True)

## GAME STATES
if st.session_state.game_state == 'start':
    st.title("💕 **Chase the Moving Heart Challenge** 💕")
    st.write("⏰ **30 seconds** to click where the heart appears! It never stops moving! 🏃‍♂️💨")
    
    col1, col2 = st.columns([1,2])
    with col1:
        if st.button("🎮 **START CHASE** 🎮", use_container_width=True):
            st.session_state.game_state = 'playing'
            st.session_state.start_time = time.time()
            st.session_state.time_left = 30
            st.session_state.heart_x = 50
            st.session_state.heart_y = 50
            st.session_state.direction_x = random.choice([-1, 1])
            st.session_state.direction_y = random.choice([-1, 1])
            st.rerun()
    
    with col2:
        st.video("https://media.giphy.com/media/Jq6o5N6V2iF2I/giphy.gif")  # Animated heart demo

elif st.session_state.game_state == 'playing':
    # Update timer
    elapsed = time.time() - st.session_state.start_time
    st.session_state.time_left = max(0, 30 - elapsed)
    
    # Move heart continuously
    st.session_state.heart_x += st.session_state.direction_x * 2
    st.session_state.heart_y += st.session_state.direction_y * 1.5
    
    # Bounce off screen edges (0-100%)
    if st.session_state.heart_x <= 0 or st.session_state.heart_x >= 95:
        st.session_state.direction_x *= -1
    if st.session_state.heart_y <= 0 or st.session_state.heart_y >= 90:
        st.session_state.direction_y *= -1
    
    # Keep in bounds
    st.session_state.heart_x = max(0, min(95, st.session_state.heart_x))
    st.session_state.heart_y = max(0, min(90, st.session_state.heart_y))
    
    # Header with timer
    col_t1, col_t2 = st.columns([2,1])
    with col_t1: st.markdown(f"### 🏃‍♂️ **Heart Position: X:{int(st.session_state.heart_x)} Y:{int(st.session_state.heart_y)}**")
    with col_t2: st.markdown(f"## ⏰ **{st.session_state.time_left:.1f}s** ⏰")
    
    # FULL SCREEN GAME ZONE
    st.markdown('<div class="game-zone">', unsafe_allow_html=True)
    
    # MOVING HEART DISPLAY (NON-CLICKABLE)
    heart_style = f"""
    <div style="
        position: absolute; 
        left: {st.session_state.heart_x}%; 
        top: {st.session_state.heart_y}%; 
        font-size: 70px;
        pointer-events: none;
        z-index: 1000;
        animation: pulse 0.5s infinite;
        text-shadow: 0 0 20px #ff1493;
    ">
        💖
    </div>
    <style>
    @keyframes pulse {{ 0% {{ transform: scale(1); }} 50% {{ transform: scale(1.2); }} 100% {{ transform: scale(1); }} }}
    </style>
    """
    st.markdown(heart_style, unsafe_allow_html=True)
    
    # CLICKABLE TARGET ZONES (5x5 grid)
    st.markdown("### **Click the zones nearest the heart! 🎯**")
    for row in range(5):
        cols = st.columns(5)
        for col in range(5):
            zone_x = col * 20
            zone_y = row * 20
            distance = abs(zone_x - st.session_state.heart_x) + abs(zone_y - st.session_state.heart_y)
            
            with cols[col]:
                if st.button(f"[{zone_x}-{zone_x+20}]
[{zone_y}-{zone_y+20}]", key=f"zone_{row}_{col}"):
                    if distance < 25:  # Close enough to heart
                        st.session_state.game_state = 'won'
                        st.success("🎉 **GOT THE HEART! Perfect timing!** 💕")
                        st.balloons()
                        st.rerun()
                    else:
                        st.error("💥 Too far! Keep chasing!")
                        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Time up check
    if st.session_state.time_left <= 0:
        st.session_state.game_state = 'lost'
        st.error("💔 **TIME UP! Heart got away!** 😭")
        st.rerun()

elif st.session_state.game_state == 'lost':
    st.markdown("## 💥 **HEART ESCAPED! PENALTY DARES** 💥")
    
    dares = [
        "💃 **Do 10 pushups** for chasing fitness! 💪",
        "🎵 **Sing 'Perfect' by Ed Sheeran** (record it!) 🎤", 
        "🍫 **Share chocolates** with someone special! 🍫",
        "✍️ **Write 3 things you love** about someone ❤️",
        "🌹 **Send flowers emoji** to 5 friends! 🌺"
    ]
    
    dare_choice = st.radio("Pick your Valentine redemption dare:", dares)
    if st.button("✅ **I ACCEPT!**", use_container_width=True):
        st.session_state.game_state = 'dare_selected'
        st.balloons()
        st.rerun()

elif st.session_state.game_state == 'dare_selected':
    st.success("✅ **Dare assigned! Complete it to become heart-catching pro!** 💖")

# ALWAYS SHOW RESTART
st.markdown("---")
if st.button("🔄 **NEW CHASE**", use_container_width=True, key="restart"):
    for key in list(st.session_state.keys()):
        if key not in ['game_state']:
            del st.session_state[key]
    st.session_state.game_state = 'start'
    st.rerun()

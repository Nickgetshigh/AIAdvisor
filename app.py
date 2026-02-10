import streamlit as st
import time
import random

st.set_page_config(page_title="💔 Catch the Elusive Heart 💔", page_icon="❤️")

# Initialize session state
if 'game_state' not in st.session_state:
    st.session_state.game_state = 'start'  # start, playing, lost, dare_selected
if 'start_time' not in st.session_state:
    st.session_state.start_time = 0
if 'heart_pos' not in st.session_state:
    st.session_state.heart_pos = (0, 0)
if 'time_left' not in st.session_state:
    st.session_state.time_left = 30

st.markdown("""
<style>
.main {background: linear-gradient(45deg, #ff69b4, #ff1493);}
.stButton > button {height: 120px; width: 120px; font-size: 40px; border-radius: 50%;}
</style>
""", unsafe_allow_html=True)

## GAME LOGIC
if st.session_state.game_state == 'start':
    st.title("💕 **Catch the Elusive Heart Challenge** 💕")
    st.write("Click the ❤️ within 30 seconds! It keeps moving... Good luck! 😈")
    
    if st.button("🎮 **START CHALLENGE** 🎮", use_container_width=True):
        st.session_state.game_state = 'playing'
        st.session_state.start_time = time.time()
        st.session_state.time_left = 30
        st.session_state.heart_pos = (random.randint(1, 10), random.randint(1, 8))
        st.rerun()

elif st.session_state.game_state == 'playing':
    # Timer countdown
    elapsed = time.time() - st.session_state.start_time
    st.session_state.time_left = max(0, 30 - elapsed)
    
    st.markdown(f"## ⏰ **Time Left: {st.session_state.time_left:.1f}s** ⏰")
    
    # Move heart every rerun (simulates movement)
    if st.session_state.time_left > 0:
        st.session_state.heart_pos = (random.randint(1, 10), random.randint(1, 8))
    
    # GAME BOARD - 8x10 grid
    st.markdown("### **Find the Heart! 👀**")
    for row in range(1, 9):
        cols = st.columns(10)
        for col in range(1, 11):
            with cols[col-1]:
                pos_key = f"{row}_{col}"
                if st.button("❤️", key=f"heart_{row}_{col}_{int(time.time())}") and (row, col) == st.session_state.heart_pos:
                    st.session_state.game_state = 'won'
                    st.success("🎉 YOU CAUGHT IT! True love skills! 💑")
                    st.balloons()
                    st.rerun()
    
    # Check if time up
    if st.session_state.time_left <= 0:
        st.session_state.game_state = 'lost'
        st.error("💥 **TIME UP! The heart escaped!** 😭")
        st.rerun()

elif st.session_state.game_state == 'lost':
    st.markdown("## 💔 **HEART ESCAPED! PENALTY TIME** 💔")
    st.write("Pick a **Valentine Dare** to redeem yourself! 😜")
    
    dares = [
        "💃 **Dance like nobody's watching** (Send video!)",
        "🍫 **Buy chocolates for your crush** (Receipt proof!)", 
        "📝 **Write a love poem** (Share screenshot!)",
        "🎤 **Sing a love song** (Voice note dare!)",
        "🌹 **Gift a flower** (Photo evidence!)"
    ]
    
    dare_choice = st.radio("Choose your dare:", dares, key="dare_select")
    
    if st.button("✅ **I ACCEPT THIS DARE!**", use_container_width=True):
        st.session_state.game_state = 'dare_selected'
        st.success(f"**Great choice! Complete: '{dare_choice}'** 🎉")
        st.balloons()
        st.rerun()

elif st.session_state.game_state == 'dare_selected':
    st.success("✅ **Dare assigned! Share proof to play again!** 💕")
    
# Play Again Button (all states)
if st.button("🔄 **NEW GAME**", key="restart"):
    for key in st.session_state:
        if key not in ['game_state']:
            del st.session_state[key]
    st.session_state.game_state = 'start'
    st.rerun()

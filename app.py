import streamlit as st
import time
import random

st.set_page_config(page_title="🌺 Jalebi Swirl Challenge 🌺", page_icon="🧡", layout="wide")

# ENHANCED MOBILE-FRIENDLY DESI CSS
st.markdown("""
<style>
html, body { 
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
    background: linear-gradient(135deg, #ff6b35, #f7931e, #ffcc02, #ff6b35) !important;
    background-size: 400% 400% !important;
    animation: gradientShift 8s ease infinite !important;
    margin: 0 !important; padding: 0 !important; overflow-x: hidden !important;
}
@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.main { 
    max-width: 420px !important; margin: 0 auto !important; padding: 1rem !important;
    background: rgba(255,255,255,0.97) !important; border-radius: 30px !important;
    box-shadow: 0 25px 70px rgba(255,107,53,0.5) !important;
    border: 3px solid rgba(255,204,2,0.3) !important;
}
header, footer { display: none !important; }
.stButton > button { 
    width: 100% !important; height: 80px !important; 
    background: linear-gradient(45deg, #ff6b35, #f7931e, #ffcc02) !important;
    background-size: 200% 200% !important;
    animation: buttonGlow 3s ease infinite !important;
    color: white !important; font-size: 24px !important; font-weight: bold !important;
    border-radius: 25px !important; border: 3px solid rgba(255,255,255,0.3) !important;
    margin: 15px 0 !important; box-shadow: 0 15px 40px rgba(255,107,53,0.5) !important;
    transition: all 0.3s ease !important;
}
.stButton > button:hover { transform: translateY(-3px) !important; box-shadow: 0 20px 50px rgba(255,107,53,0.7) !important; }
@keyframes buttonGlow {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}
.jalebi-frame {
    position: relative; height: 450px; 
    background: linear-gradient(45deg, rgba(255,204,2,0.3), rgba(255,107,53,0.2));
    border: 4px solid #ffcc02; border-radius: 25px; overflow: hidden; margin: 25px 0;
    box-shadow: inset 0 0 50px rgba(255,204,2,0.3), 0 10px 30px rgba(0,0,0,0.2);
}
.jalebi {
    position: absolute; font-size: 100px; cursor: pointer; z-index: 10;
    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    text-shadow: 0 0 30px #ffcc02, 0 0 40px #f7931e;
    animation: jalebiFloat 2s ease-in-out infinite;
}
@keyframes jalebiFloat {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-15px) rotate(10deg); }
}
.jalebi:hover { 
    transform: scale(1.4) !important; animation: jalebiWiggle 0.3s !important; 
    filter: drop-shadow(0 0 50px #ffcc02) !important;
}
@keyframes jalebiWiggle {
    0%, 100% { transform: scale(1.4) rotate(0deg); }
    25% { transform: scale(1.5) rotate(8deg); }
    75% { transform: scale(1.5) rotate(-8deg); }
}
.stats-bar {
    background: linear-gradient(90deg, #ff6b35, #f7931e, #ffcc02); 
    background-size: 200% 200%; animation: statsGlow 2s ease infinite;
    color: white; padding: 20px; border-radius: 20px; text-align: center; 
    font-size: 24px; font-weight: bold; margin: 15px 0; text-shadow: 0 0 10px rgba(0,0,0,0.5);
}
@keyframes statsGlow { 0%, 100% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } }
.glitch { 
    animation: glitch 0.2s infinite !important; color: #ff1744 !important; 
    text-shadow: 2px 0 #ff1744, -2px 0 #00ff00, 0 2px #00ff00 !important;
}
@keyframes glitch {
    0%, 100% { transform: translate(0); }
    10% { transform: translate(-2px, 2px); }
    20% { transform: translate(2px, -2px); }
    30% { transform: translate(-2px, -2px); }
    40% { transform: translate(2px, 2px); }
}
.penalty-card {
    background: linear-gradient(135deg, rgba(255,107,53,0.95), rgba(247,147,30,0.95)); 
    color: white; padding: 40px; border-radius: 30px; text-align: center; margin: 30px 0;
    box-shadow: 0 20px 60px rgba(255,107,53,0.6); 
    border: 5px solid #ffcc02; position: relative; overflow: hidden;
}
.penalty-card::before {
    content: '🎁'; position: absolute; top: 20px; right: 20px; font-size: 60px; opacity: 0.3;
}
.penalty-card::after {
    content: '💕'; position: absolute; bottom: 20px; left: 20px; font-size: 50px; opacity: 0.3;
}
.nikku-name { color: #ffcc02 !important; font-size: 32px !important; font-weight: bold !important; text-shadow: 0 0 20px #ffcc02 !important; }
</style>
""", unsafe_allow_html=True)

# SESSION STATE
if 'game_state' not in st.session_state: st.session_state.game_state = 'start'
if 'start_time' not in st.session_state: st.session_state.start_time = 0
if 'clicks' not in st.session_state: st.session_state.clicks = 0
if 'jalebi_x' not in st.session_state: st.session_state.jalebi_x = 50
if 'jalebi_y' not in st.session_state: st.session_state.jalebi_y = 50

def new_jalebi_position():
    st.session_state.jalebi_x = random.randint(12, 88)
    st.session_state.jalebi_y = random.randint(12, 88)

if st.session_state.game_state == 'start':
    st.markdown("## 🌺 **JALEBI SWIRL CHALLENGE** 🌺")
    st.markdown("<h3 style='color: #ff6b35; text-align: center;'>🍬 **Catch 3 swirling jalebis before they escape!** 🍬</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px; color: #f7931e;'>Pro tip: They'll swirl faster than you can swipe! 😏</p>", unsafe_allow_html=True)
    
    if st.button("🧡 **START SWEET CHASE** 🧡"):
        st.session_state.game_state = 'playing'
        st.session_state.start_time = time.time()
        st.session_state.clicks = 0
        new_jalebi_position()
        st.rerun()

elif st.session_state.game_state == 'playing':
    elapsed = time.time() - st.session_state.start_time
    time_left = max(0, 10 - elapsed)
    
    # ENHANCED STATS BAR
    st.markdown(f"""
    <div class="stats-bar">
        ⏰ **{time_left:.1f}s LEFT** | 🧡 **{st.session_state.clicks}/3 JALEBIS** | ✨ **SWIRL MODE**
    </div>
    """, unsafe_allow_html=True)
    
    # UPGRADED JALEBI FRAME
    st.markdown('<div class="jalebi-frame">', unsafe_allow_html=True)
    
    # ULTRA REALISTIC JALEBI (🧿 + 🍬 combo)
    jalebi_style = f"""
    <div class="jalebi" 
         style="left: {st.session_state.jalebi_x}%; top: {st.session_state.jalebi_y}%;
         transform: translate(-50%, -50%);">
        <div style='position: absolute; font-size: 70px;'>🧿</div>
        <div style='position: absolute; font-size: 50px; top: 10px; left: 10px;'>🍬</div>
    </div>
    """
    st.markdown(jalebi_style, unsafe_allow_html=True)
    
    # PERFECTLY ALIGNED CLICK ZONE
    col1, col2 = st.columns([2.5, 1])
    with col2:
        if st.button("🍬 **CATCH!** 🍬", key="jalebi_click", help="Tap the jalebi above!"):
            st.session_state.clicks += 1
            st.balloons()
            st.snow()
            new_jalebi_position()
            if st.session_state.clicks >= 3 or time_left <= 0:
                st.session_state.game_state = 'glitch'
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.session_state.clicks >= 3 or time_left <= 0:
        st.session_state.game_state = 'glitch'
        st.rerun()

elif st.session_state.game_state == 'glitch':
    st.markdown("""
    <div style='text-align: center; padding: 50px;'>
        <h1 class="glitch" style='font-size: 42px;'>🚨 **ERROR: SWEETNESS OVERLOAD!** 🚨</h1>
        <h2 class="glitch" style='font-size: 32px;'>**JALEBI SYSTEM CRASH** 💥🍬💻</h2>
        <div style='font-size: 24px; color: #ff1744; animation: shake 0.5s infinite;'>[CRASH LOG: TOO MUCH DESI LOVE]</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="penalty-card">
        <h2 style='margin-top: 0;'>😭 **JALEBIS ESCAPED! DEFEAT!** 😭</h2>
        <div style='font-size: 28px; margin: 25px 0; color: white;'>🛍️ **PENALTY BY LAW OF LOVE** 🛍️</div>
        <div style='font-size: 26px; background: rgba(255,255,255,0.25); padding: 30px; border-radius: 20px; margin: 20px 0;'>
            <div class="nikku-name">**NIKKU**</div>
            <div style='font-size: 24px; margin-top: 15px;'>**must receive:**</div>
            <div style='font-size: 28px; color: #ffcc02; margin-top: 10px;'>🎁 **NEW KURTA or HOODIE** 🎁</div>
        </div>
        <div style='font-size: 22px; margin-top: 25px; padding: 20px; background: rgba(0,0,0,0.3); border-radius: 15px;'>
            📸 **Screenshot this + shopping proof = LOVE WIN!** 💕
        </div>
        <div style='font-size: 18px; margin-top: 20px; opacity: 0.9;'>
            *Penalty enforced by Universal Desi Romance Code* ✨
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔄 **NEW JALEBI CHALLENGE** 🔄"):
        for key in list(st.session_state.keys()):
            if key != 'game_state':
                del st.session_state[key]
        st.session_state.game_state = 'start'
        st.rerun()

# DESI LOVE FOOTER
st.markdown("""
<div style='text-align: center; margin-top: 40px; color: #ff6b35; font-size: 20px; 
    background: rgba(255,204,2,0.2); padding: 20px; border-radius: 20px;'>
    💕 **Made with Pure Desi Love for Nikku** 💕<br>
    <span style='font-size: 16px; color: #f7931e;'>Valentine's Day Special | 2026</span>
</div>
""", unsafe_allow_html=True)

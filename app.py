import streamlit as st
import time

st.set_page_config(page_title="🔥 दिल का क्लिकर धमाका 🔥", page_icon="❤️")

# Initialize
if 'hearts' not in st.session_state: st.session_state.hearts = 0
if 'rupees' not in st.session_state: st.session_state.rupees = 0
if 'cps' not in st.session_state: st.session_state.cps = 0
if 'upgrades' not in st.session_state:
    st.session_state.upgrades = {'bhabhi': 0, 'padosan': 0, 'sautan': 0, 'desi_cupid': 0}
if 'last_time' not in st.session_state: st.session_state.last_time = time.time()

st.markdown("""
<style>
.main {background: linear-gradient(45deg, #ff4444, #ffaa00, #ff4444);}
.stButton > button {background: #d63384; color: gold; font-weight: bold; font-size: 24px; border: 3px solid gold;}
h1 {color: #ff1493; text-shadow: 2px 2px gold;}
.metric {font-size: 2.5em; color: #ff69b4;}
</style>
""", unsafe_allow_html=True)

## 🔥 MAIN DHAMAKA SCREEN 🔥
st.markdown("## 😂🔥 **DIL KA CLICKER DHAMAKA** 🔥😂")
st.markdown("**भाई click करो ये दिल तोड़ो! 💔 प्यार के रुपये कमाओ! हर upgrade में desi comedy!** 🎭")

col1, col2, col3 = st.columns(3)
with col1: st.metric("💔 दिल टूटे", f"{int(st.session_state.hearts):,}")
with col2: st.metric("💰 रुपये/sec", st.session_state.cps)
with col3: st.metric("😂 मसाला लेवल", sum(st.session_state.upgrades.values()))

# GIANT HEART BUTTON
if st.button("💔 **DIL TOD DO BHAI!** 💔", use_container_width=True):
    bonus = 1 + st.session_state.upgrades['bhabhi'] * 2
    st.session_state.hearts += bonus
    st.session_state.rupees += bonus * 0.1
    st.balloons()
    st.session_state.last_time = time.time()
    st.rerun()

# Auto rupees
delta = time.time() - st.session_state.last_time
st.session_state.hearts += st.session_state.cps * delta * 0.1
st.session_state.rupees += st.session_state.cps * delta
st.session_state.last_time = time.time()

## 🎭 DESI GAALI JOKES
jokes = [
    "तेरी भाभी ने like ठोका! 😂 +5 hearts",
    "पड़ोसन ने आँख मार दी! 😏 रुपये double!",
    "सौतन जल गयी! 🔥 Free boost भाई!",
    "कुत्ते ने दिल चुरा लिया! 🐕💔 हाहाहा!",
    "मम्मी ने पकड़ लिया! 😱 Game over almost!",
    "Cupid ने thappad मार दिया! 💥 +100 hearts"
]
if st.session_state.hearts > 10:
    st.error(f"**{jokes[int(st.session_state.hearts/50) % len(jokes)]}**")

## 🛒 DESI UPGRADES SHOP 🛒
st.markdown("---")
st.subheader("🛍️ **DESI UPGRADE DHABA** 🛍️")

upgrades = [
    {'name': '👩‍🦰 भाभी का झटका', 'cost': 15, 'cps': 0.2, 'key': 'bhabhi', 'emoji': '😍🔥'},
    {'name': '😘 पड़ोसन पावर', 'cost': 75, 'cps': 1, 'key': 'padosan', 'emoji': '😏💋'},
    {'name': '😡 सौतन का जलन', 'cost': 300, 'cps': 5, 'key': 'sautan', 'emoji': '🔥💥'},
    {'name': '🏹 देसी कपिड धमाल', 'cost': 1000, 'cps': 20, 'key': 'desi_cupid', 'emoji': '💘🚀'}
]

for up in upgrades:
    col1, col2 = st.columns([3,1])
    with col1:
        st.markdown(f"**{up['emoji']} {up['name']}** (x{st.session_state.upgrades[up['key']]})")
    with col2:
        if st.button(f"₹{up['cost']}", key=f"buy_{up['key']}"):
            if st.session_state.rupees >= up['cost']:
                st.session_state.rupees -= up['cost']
                st.session_state.upgrades[up['key']] += 1
                st.session_state.cps += up['cps']
                st.snow() if 'पड़ोसन' in up['name'] else st.balloons()
                st.success(f"{up['name']} खरीद ली भाई! अब कमाई होगी!")
                st.rerun()
            else:
                st.error("**पैसे कम हैं भाई! और click करो!** 😭")

# RESET
if st.button("🔄 **नया धमाल शुरू करो**", key="reset"):
    for key in st.session_state:
        if key not in ['last_time']:
            st.session_state[key] = 0 if isinstance(st.session_state[key], int) else {}
    st.rerun()

# VICTORY
if st.session_state.hearts >= 5000:
    st.markdown("""
    <div style='text-align:center; background:gold; padding:20px; border-radius:15px;'>
    <h1>🎉 **TRUE INDIAN LOVE BOSS** 🎉</h1>
    <h2>5000+ दिल तोड़े! पूरा मोहल्ला जल गया! 🔥😂</h2>
    </div>
    """, unsafe_allow_html=True)
    st.balloons()
    st.snow()

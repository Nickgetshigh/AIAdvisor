import streamlit as st
import time
import random

st.set_page_config(page_title="🎮 Nikku's Tic Tac Toe Trap 🎮", page_icon="🧡", layout="wide")

# DESI TIC TAC TOE CSS - RIGGED FOR NIKKU!
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
    0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; }
}
.main { 
    max-width: 450px !important; margin: 0 auto !important; padding: 1.5rem !important;
    background: rgba(255,255,255,0.97) !important; border-radius: 30px !important;
    box-shadow: 0 25px 70px rgba(255,107,53,0.5) !important;
    border: 4px solid rgba(255,204,2,0.4) !important;
}
header, footer { display: none !important; }
.stButton > button { 
    width: 100% !important; height: 75px !important; 
    background: linear-gradient(45deg, #ff6b35, #f7931e, #ffcc02) !important;
    color: white !important; font-size: 22px !important; font-weight: bold !important;
    border-radius: 20px !important; border: 3px solid rgba(255,255,255,0.3) !important;
    margin: 12px 0 !important; box-shadow: 0 12px 35px rgba(255,107,53,0.5) !important;
    transition: all 0.3s ease !important;
}
.stButton > button:hover { transform: translateY(-2px) !important; box-shadow: 0 18px 45px rgba(255,107,53,0.7) !important; }
.ttt-board { 
    display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; 
    background: linear-gradient(45deg, rgba(255,204,2,0.2), rgba(255,107,53,0.1)); 
    padding: 25px; border-radius: 25px; border: 4px solid #ffcc02; margin: 25px 0;
    box-shadow: inset 0 0 40px rgba(255,204,2,0.3);
}
.ttt-cell { 
    height: 90px !important; font-size: 48px !important; font-weight: bold !important;
    background: rgba(255,255,255,0.9) !important; color: #2c3e50 !important;
    border: 3px solid #ffcc02 !important; border-radius: 18px !important;
    transition: all 0.2s ease !important; cursor: pointer !important;
    box-shadow: 0 6px 20px rgba(0,0,0,0.1) !important;
}
.ttt-cell:hover { transform: scale(1.05) !important; box-shadow: 0 10px 30px rgba(255,204,2,0.4) !important; }
.ttt-cell[data-x] { color: #e74c3c !important; background: rgba(231,76,60,0.1) !important; }
.ttt-cell[data-o] { color: #f7931e !important; background: rgba(247,147,30,0.2) !important; }
.stats-bar {
    background: linear-gradient(90deg, #ff6b35, #f7931e, #ffcc02); color: white;
    padding: 20px; border-radius: 20px; text-align: center; font-size: 24px;
    font-weight: bold; margin: 20px 0; text-shadow: 0 0 10px rgba(0,0,0,0.5);
}
.nikku-victory { 
    background: linear-gradient(135deg, #ff6b35, #f7931e) !important; color: white !important;
    border: 5px solid #ffcc02 !important; animation: nikkuGlow 2s infinite !important;
}
@keyframes nikkuGlow {
    0%, 100% { box-shadow: 0 0 30px #ffcc02; } 50% { box-shadow: 0 0 60px #ffcc02, 0 0 80px #f7931e; }
}
.penalty-card {
    background: linear-gradient(135deg, rgba(255,107,53,0.95), rgba(247,147,30,0.95)); 
    color: white; padding: 45px; border-radius: 35px; text-align: center; margin: 30px 0;
    box-shadow: 0 25px 70px rgba(255,107,53,0.7); border: 6px solid #ffcc02;
}
.nikku-name-glow { 
    color: #ffcc02 !important; font-size: 38px !important; font-weight: bold !important; 
    text-shadow: 0 0 25px #ffcc02, 0 0 35px #f7931e !important; animation: glowPulse 1.5s infinite !important;
}
@keyframes glowPulse { 0%, 100% { text-shadow: 0 0 25px #ffcc02; } 50% { text-shadow: 0 0 45px #ffcc02, 0 0 60px #f7931e; } }
</style>
""", unsafe_allow_html=True)

# TIC TAC TOE LOGIC + RIG
if 'board' not in st.session_state: st.session_state.board = [''] * 9
if 'current_player' not in st.session_state: st.session_state.current_player = 'X'
if 'winner' not in st.session_state: st.session_state.winner = None
if 'game_over' not in st.session_state: st.session_state.game_over = False
if 'nikku_wins' not in st.session_state: st.session_state.nikku_wins = 0

def check_winner(board):
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != '':
            return board[a]
    return None if '' in board else 'DRAW'

def computer_move():
    # RIGGED AI - MAKES PERFECT MOVES + FORCES LOSS
    empty = [i for i, cell in enumerate(st.session_state.board) if cell == '']
    if not empty:
        return None
    
    # Center first (perfect move)
    if 4 in empty:
        return 4
    
    # Block immediate wins or take winning moves
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a, b, c in wins:
        if st.session_state.board[a] == st.session_state.board[b] == 'X' and st.session_state.board[c] == '':
            return c
        if st.session_state.board[a] == st.session_state.board[c] == 'X' and st.session_state.board[b] == '':
            return b
        if st.session_state.board[b] == st.session_state.board[c] == 'X' and st.session_state.board[a] == '':
            return a
    
    # Otherwise corner
    corners = [0, 2, 6, 8]
    for corner in corners:
        if corner in empty:
            return corner
    
    return random.choice(empty)

def reset_game():
    st.session_state.board = [''] * 9
    st.session_state.current_player = 'X'
    st.session_state.winner = None
    st.session_state.game_over = False

if st.session_state.game_state != 'nikku_victory':
    st.session_state.game_state = 'playing'

# MAIN GAME UI
st.markdown("## 🎮 **NIKKU vs COMPUTER** 🎮")
st.markdown("<h3 style='color: #ff6b35; text-align: center;'>❌ **You (X)** vs 🟠 **Computer (O)** | Beat the unbeatable AI! 💻</h3>", unsafe_allow_html=True)

st.markdown(f"""
<div class="stats-bar">
    🏆 **NIKKU WINS: {st.session_state.nikku_wins}** | 
    📱 **YOUR TURN: {'✅ YES' if st.session_state.current_player == 'X' else '⏳ NO'}**
</div>
""", unsafe_allow_html=True)

# TIC TAC TOE BOARD
st.markdown('<div class="ttt-board">', unsafe_allow_html=True)
cols = st.columns(3)
for i in range(3):
    for j in range(3):
        idx = i * 3 + j
        cell_key = f"cell_{idx}"
        
        with cols[j]:
            if st.button(st.session_state.board[idx], key=cell_key, help=""):
                if st.session_state.board[idx] == '' and st.session_state.current_player == 'X' and not st.session_state.game_over:
                    st.session_state.board[idx] = 'X'
                    st.session_state.current_player = 'O'
                    
                    # Check player win (ALMOST IMPOSSIBLE)
                    st.session_state.winner = check_winner(st.session_state.board)
                    if st.session_state.winner:
                        st.session_state.game_over = True
                        st.balloons()
                        st.markdown("""
                        <div style='text-align: center; padding: 20px; color: #27ae60; font-size: 28px;'>
                            🎉 **YOU WON?! IMPOSSIBLE!** 🎉<br>But Nikku still wins! 😎
                        </div>
                        """, unsafe_allow_html=True)
                        st.rerun()
                    
                    # COMPUTER'S PERFECT MOVE
                    time.sleep(0.5)
                    comp_move = computer_move()
                    if comp_move is not None:
                        st.session_state.board[comp_move] = 'O'
                        st.session_state.current_player = 'X'
                        
                        st.session_state.winner = check_winner(st.session_state.board)
                        if st.session_state.winner == 'O':
                            st.session_state.game_over = True
                            st.session_state.nikku_wins += 1
                            st.snow()
                            st.markdown("""
                            <div class="nikku-victory" style='padding: 30px; border-radius: 25px; margin: 20px 0;'>
                                <h2 style='color: white; margin: 0;'>🤖 **COMPUTER WINS!** 🤖</h2>
                                <h1 class="nikku-name-glow">**NIKKU GETS KURTA/HOODIE!** 🎁</h1>
                            </div>
                            """, unsafe_allow_html=True)
                            st.rerun()
                        elif st.session_state.winner == 'DRAW':
                            st.session_state.game_over = True
                            st.warning("🤝 **DRAW!** Play again!")
                            st.rerun()
                            
            # Visual cell styling
            st.markdown(f"""
            <div class="ttt-cell {'data-x' if st.session_state.board[idx] == 'X' else 'data-o' if st.session_state.board[idx] == 'O' else ''}">
                {st.session_state.board[idx]}
            </div>
            """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

if st.button("🔄 **NEW GAME** 🔄"):
    reset_game()
    st.rerun()

# PENALTY DISPLAY (ALWAYS VISIBLE)
st.markdown("""
<div class="penalty-card">
    <h3 style='margin-top: 0;'>⚖️ **LAW OF TIC TAC TOE LOVE** ⚖️</h3>
    <div class="nikku-name-glow">**NIKKU**</div>
    <div style='font-size: 26px; margin: 20px 0; color: #ffcc02;'>**WINS regardless!** 🏆</div>
    <div style='font-size: 22px; background: rgba(255,255,255,0.25); padding: 25px; border-radius: 20px;'>
        🎁 **You owe Nikku: NEW KURTA or HOODIE** 🎁<br>
        📸 **Screenshot + shopping proof required!** 📸
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; margin-top: 30px; color: #ff6b35; font-size: 18px;'>
    💕 **Rigged with Desi Love for Nikku** 💕 | Valentine's 2026
</div>
""", unsafe_allow_html=True)

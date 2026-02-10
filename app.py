import streamlit as st
import time
import random

st.set_page_config(page_title="🎮 Nikku's Tic Tac Toe Trap 🎮", page_icon="🧡", layout="wide")

# PROPER SESSION STATE INITIALIZATION
if 'board' not in st.session_state:
    st.session_state.board = [''] * 9
if 'current_player' not in st.session_state:
    st.session_state.current_player = 'X'
if 'winner' not in st.session_state:
    st.session_state.winner = None
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'nikku_wins' not in st.session_state:
    st.session_state.nikku_wins = 0
if 'game_state' not in st.session_state:
    st.session_state.game_state = 'playing'

# DESI TIC TAC TOE CSS
st.markdown("""
<style>
.main { max-width: 450px !important; margin: 0 auto !important; padding: 1.5rem !important;
    background: rgba(255,255,255,0.97) !important; border-radius: 30px !important;
    box-shadow: 0 25px 70px rgba(255,107,53,0.5) !important; border: 4px solid rgba(255,204,2,0.4) !important;
    background: linear-gradient(135deg, #ff6b35, #f7931e, #ffcc02, #ff6b35) !important; }
header, footer { display: none !important; }
.stButton > button { width: 100% !important; height: 75px !important; 
    background: linear-gradient(45deg, #ff6b35, #f7931e, #ffcc02) !important; color: white !important; 
    font-size: 22px !important; font-weight: bold !important; border-radius: 20px !important; 
    border: 3px solid rgba(255,255,255,0.3) !important; margin: 12px 0 !important; 
    box-shadow: 0 12px 35px rgba(255,107,53,0.5) !important; }
.ttt-board { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; 
    background: linear-gradient(45deg, rgba(255,204,2,0.2), rgba(255,107,53,0.1)); 
    padding: 25px; border-radius: 25px; border: 4px solid #ffcc02; margin: 25px 0;
    box-shadow: inset 0 0 40px rgba(255,204,2,0.3); }
.ttt-cell { height: 90px !important; font-size: 48px !important; font-weight: bold !important;
    background: rgba(255,255,255,0.9) !important; color: #2c3e50 !important;
    border: 3px solid #ffcc02 !important; border-radius: 18px !important; cursor: pointer !important;
    box-shadow: 0 6px 20px rgba(0,0,0,0.1) !important; }
.ttt-cell:hover { transform: scale(1.05) !important; box-shadow: 0 10px 30px rgba(255,204,2,0.4) !important; }
.nikku-victory { background: linear-gradient(135deg, #ff6b35, #f7931e) !important; 
    color: white !important; border: 5px solid #ffcc02 !important; padding: 30px; 
    border-radius: 25px; margin: 20px 0; text-align: center; }
.nikku-name-glow { color: #ffcc02 !important; font-size: 38px !important; font-weight: bold !important; 
    text-shadow: 0 0 25px #ffcc02 !important; }
.stats-bar { background: linear-gradient(90deg, #ff6b35, #f7931e, #ffcc02); 
    color: white; padding: 20px; border-radius: 20px; text-align: center; font-size: 24px;
    font-weight: bold; margin: 20px 0; }
.penalty-card { background: linear-gradient(135deg, rgba(255,107,53,0.95), rgba(247,147,30,0.95)); 
    color: white; padding: 45px; border-radius: 35px; text-align: center; margin: 30px 0;
    box-shadow: 0 25px 70px rgba(255,107,53,0.7); border: 6px solid #ffcc02; }
</style>
""", unsafe_allow_html=True)

def check_winner(board):
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != '':
            return board[a]
    return None if '' in board else 'DRAW'

def computer_move():
    empty = [i for i, cell in enumerate(st.session_state.board) if cell == '']
    if not empty:
        return None
    
    # UNBEATABLE AI STRATEGY
    if 4 in empty:  # Center first
        return 4
    
    # Block wins / take wins
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a, b, c in wins:
        if st.session_state.board[a] == st.session_state.board[b] == 'X' and st.session_state.board[c] == '':
            return c
        if st.session_state.board[a] == st.session_state.board[c] == 'X' and st.session_state.board[b] == '':
            return b
        if st.session_state.board[b] == st.session_state.board[c] == 'X' and st.session_state.board[a] == '':
            return a
    
    # Corners
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

# MAIN UI
st.markdown("## 🎮 **NIKKU vs UNBEATABLE AI** 🎮")
st.markdown("<h3 style='color: #ff6b35; text-align: center;'>❌ **You (X)** vs 🟠 **Computer (O)**</h3>", unsafe_allow_html=True)

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
        
        with cols[j]:
            if st.button(st.session_state.board[idx], key=f"cell_{idx}"):
                if (st.session_state.board[idx] == '' and 
                    st.session_state.current_player == 'X' and 
                    not st.session_state.game_over):
                    
                    st.session_state.board[idx] = 'X'
                    st.session_state.current_player = 'O'
                    
                    # Check player win (RARE!)
                    st.session_state.winner = check_winner(st.session_state.board)
                    if st.session_state.winner == 'X':
                        st.session_state.game_over = True
                        st.session_state.nikku_wins += 1  # Nikku still wins!
                        st.balloons()
                        st.markdown("""
                        <div class="nikku-victory">
                            <h2>🎉 **YOU WON THE GAME!** 🎉</h2>
                            <h1 class="nikku-name-glow">**But NIKKU still wins the prize!** 😎</h1>
                        </div>
                        """, unsafe_allow_html=True)
                        st.rerun()
                    
                    # COMPUTER'S PERFECT TURN
                    if not st.session_state.game_over:
                        time.sleep(0.8)  # Dramatic pause
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
                                <div class="nikku-victory">
                                    <h2>🤖 **COMPUTER WINS!** 🤖</h2>
                                    <h1 class="nikku-name-glow">**NIKKU GETS KURTA/HOODIE!** 🎁</h1>
                                </div>
                                """, unsafe_allow_html=True)
                                st.rerun()
                            elif st.session_state.winner == 'DRAW':
                                st.session_state.game_over = True
                                st.warning("🤝 **DRAW!** Nikku still wins!")
                                st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# CONTROLS
col1, col2 = st.columns(2)
with col1:
    if st.button("🔄 **NEW GAME** 🔄"):
        reset_game()
        st.rerun()

# ALWAYS VISIBLE PENALTY
st.markdown("""
<div class="penalty-card">
    <h3>⚖️ **LAW OF TIC TAC TOE LOVE** ⚖️</h3>
    <div class="nikku-name-glow">**NIKKU**</div>
    <div style='font-size: 26px; margin: 20px 0; color: #ffcc02;'>**WINS EVERY TIME!** 🏆</div>
    <div style='font-size: 22px; background: rgba(255,255,255,0.25); padding: 25px; border-radius: 20px;'>
        🎁 **You owe Nikku: NEW KURTA or HOODIE** 🎁<br>
        📸 **Screenshot + shopping proof = LOVE WIN!** 📸
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; margin-top: 30px; color: white; font-size: 18px; 
    background: rgba(255,107,53,0.3); padding: 20px; border-radius: 20px;'>
    💕 **Rigged with Pure Desi Love for Nikku** 💕 | Valentine's 2026
</div>
""", unsafe_allow_html=True)

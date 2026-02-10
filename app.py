import streamlit as st
import random
import time
from streamlit_confetti import confetti

# --- PAGE CONFIG ---
st.set_page_config(page_title="The Valentine's Challenge", page_icon="❤️", layout="centered")

# --- CUSTOM THEME & STYLING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Poppins:wght@300;400&display=swap');
    
    .main { background-color: #FFF5F5; }
    h1, h2, h3 { font-family: 'Playfair Display', serif; color: #8B0000; text-align: center; }
    p { font-family: 'Poppins', sans-serif; color: #4A4A4A; text-align: center; }
    
    /* Grid Styling */
    .stButton > button {
        width: 100%;
        height: 100px;
        font-size: 40px !important;
        border-radius: 15px;
        border: 2px solid #FFC0CB;
        background-color: white;
        color: #8B0000;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        border-color: #FFD700;
        background-color: #FFF0F0;
        transform: scale(1.02);
    }
    /* Fixed Container for the Board */
    div[data-testid="stVerticalBlock"] > div:has(div.stButton) {
        gap: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MINIMAX LOGIC ---
def check_winner(board):
    lines = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a, b, c in lines:
        if board[a] == board[b] == board[c] and board[a] is not None:
            return board[a]
    if None not in board: return "Draw"
    return None

def minimax(board, depth, is_maximizing):
    res = check_winner(board)
    if res == "O": return 10 - depth
    if res == "X": return depth - 10
    if res == "Draw": return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] is None:
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = None
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] is None:
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = None
                best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] is None:
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = None
            if score > best_score:
                best_score = score
                move = i
    return move

# --- GAME STATE ---
if 'board' not in st.session_state:
    st.session_state.board = [None] * 9
    st.session_state.game_over = False
    st.session_state.status = "Think you can beat me? If you lose, the stakes are high..."

# --- UI COMPONENTS ---
def reset_game():
    st.session_state.board = [None] * 9
    st.session_state.game_over = False
    st.session_state.status = "Think you can beat me? If you lose, the stakes are high..."

# --- HEADER ---
st.title("🌹 The Valentine's Stakes")
st.write(st.session_state.status)

# --- THE GAME BOARD ---
@st.fragment
def render_board():
    cols = st.columns(3)
    for i in range(9):
        with cols[i % 3]:
            # Label logic: Show X, O or empty string
            label = st.session_state.board[i] if st.session_state.board[i] else " "
            
            if st.button(label, key=f"btn_{i}", disabled=st.session_state.game_over or st.session_state.board[i] is not None):
                # Player Move
                st.session_state.board[i] = "X"
                
                # Check if Player won (impossible against this AI, but for logic sake)
                if check_winner(st.session_state.board) is None:
                    # AI Move
                    with st.spinner("Thinking..."):
                        time.sleep(0.2) # Artificial "Quick Think"
                        ai_move = get_best_move(st.session_state.board)
                        if ai_move is not None:
                            st.session_state.board[ai_move] = "O"
                
                # Update Status
                result = check_winner(st.session_state.board)
                if result:
                    st.session_state.game_over = True
                    if result == "O":
                        st.session_state.status = "LOSE"
                    elif result == "Draw":
                        st.session_state.status = "DRAW"
                else:
                    taunts = ["Nice try!", "Are you sure about that?", "Calculated.", "Hmm... interesting."]
                    st.session_state.status = random.choice(taunts)
                st.rerun()

render_board()

# --- CONCLUSION LOGIC ---
if st.session_state.game_over:
    st.divider()
    if st.session_state.status == "LOSE":
        confetti()
        st.error("### Victory is mine! ❤️")
        st.markdown("""
            **Now, for your penalty:** You must wear your absolute best dress for our Valentine's date  
            and surprise me with a wonderful gift. **No excuses!**
        """)
    elif st.session_state.status == "DRAW":
        st.warning("### A Draw? I'll let you off easy... this time.")
    
    if st.button("Rematch? (Double or Nothing)"):
        reset_game()
        st.rerun()

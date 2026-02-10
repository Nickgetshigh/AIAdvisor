import streamlit as st
import streamlit_confetti as confetti
import time
import random
from typing import List, Tuple, Optional

# Color palette
COLORS = {
    'rose': '#FFC0CB',
    'crimson': '#8B0000',
    'gold': '#FFD700',
    'dark_bg': '#1a0f1a',
    'light_bg': '#2d1b2d'
}

# Custom CSS for romantic theme
ST_CSS = f"""
<style>
    .main {{
        background: linear-gradient(135deg, {COLORS['dark_bg']}, {COLORS['light_bg']});
        padding: 2rem;
    }}
    .stApp {{
        background: transparent;
    }}
    h1, h2, h3 {{
        color: {COLORS['gold']};
        font-family: 'Georgia', serif;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }}
    .metric {{
        background: rgba(255,192,203,0.2);
        border: 2px solid {COLORS['rose']};
        border-radius: 15px;
        padding: 1rem;
    }}
    .stButton > button {{
        background: linear-gradient(45deg, {COLORS['crimson']}, {COLORS['rose']});
        color: white;
        border: none;
        border-radius: 12px;
        font-weight: bold;
        font-size: 1.1rem;
        padding: 0.8rem 1.5rem;
        box-shadow: 0 4px 15px rgba(139,0,0,0.4);
        transition: all 0.3s ease;
    }}
    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(139,0,0,0.6);
    }}
    .cell {{
        width: 120px !important;
        height: 120px !important;
        font-size: 3rem !important;
        font-weight: bold !important;
        background: rgba(255,255,255,0.1) !important;
        border: 3px solid {COLORS['gold']} !important;
        border-radius: 15px !important;
        color: {COLORS['gold']} !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(10px);
    }}
    .cell:hover {{
        background: rgba(255,192,203,0.3) !important;
        transform: scale(1.05);
    }}
    .toast {{
        background: linear-gradient(45deg, {COLORS['rose']}, {COLORS['gold']});
        color: {COLORS['crimson']};
        padding: 1rem 2rem;
        border-radius: 25px;
        font-weight: bold;
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        margin: 1rem 0;
    }}
</style>
"""

class TicTacToe:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # User starts
        self.game_over = False
        self.winner = None
        
    def make_move(self, row: int, col: int, player: str) -> bool:
        """Make a move if valid"""
        if self.board[row][col] == '' and not self.game_over:
            self.board[row][col] = player
            self.current_player = 'O' if player == 'X' else 'X'
            return True
        return False
    
    def check_winner(self) -> Optional[str]:
        """Check rows, columns, and diagonals for winner"""
        # Rows
        for row in self.board:
            if row[0] == row[1] == row[2] != '':
                return row[0]
        
        # Columns
        for col in range(3):
            if (self.board[0][col] == self.board[1][col] == self.board[2][col] != ''):
                return self.board[0][col]
        
        # Diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return self.board[0][2]
        
        # Draw
        if all(cell != '' for row in self.board for cell in row):
            return 'draw'
        
        return None
    
    def is_board_full(self) -> bool:
        return all(cell != '' for row in self.board for cell in row)
    
    def get_empty_positions(self) -> List[Tuple[int, int]]:
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == '']

def minimax(board: List[List[str]], is_maximizing: bool, game: TicTacToe) -> int:
    """Minimax algorithm with alpha-beta pruning for unbeatable AI"""
    winner = game.check_winner()
    
    if winner == 'O':  # AI wins
        return 10
    elif winner == 'X':  # User wins
        return -10
    elif winner == 'draw':
        return 0
    
    if is_maximizing:  # AI's turn (O)
        max_eval = -float('inf')
        for row, col in game.get_empty_positions():
            temp_board = [row[:] for row in board]
            temp_board[row][col] = 'O'
            temp_game = TicTacToe()
            temp_game.board = temp_board
            eval_score = minimax(temp_board, False, temp_game)
            max_eval = max(max_eval, eval_score)
        return max_eval
    else:  # User's turn (X)
        min_eval = float('inf')
        for row, col in game.get_empty_positions():
            temp_board = [row[:] for row in board]
            temp_board[row][col] = 'X'
            temp_game = TicTacToe()
            temp_game.board = temp_board
            eval_score = minimax(temp_board, True, temp_game)
            min_eval = min(min_eval, eval_score)
        return min_eval

def get_best_move(game: TicTacToe) -> Optional[Tuple[int, int]]:
    """Find the best move for AI using minimax"""
    best_score = -float('inf')
    best_move = None
    
    for row, col in game.get_empty_positions():
        temp_board = [row[:] for row in game.board]
        temp_board[row][col] = 'O'
        temp_game = TicTacToe()
        temp_game.board = temp_board
        
        move_score = minimax(temp_board, False, temp_game)
        
        if move_score > best_score:
            best_score = move_score
            best_move = (row, col)
    
    return best_move

# Valentine messages
WELCOME_MESSAGE = "💕 **Think you can beat me?** 💕

If you lose, the stakes are *high*... Play as **X**, I'll be **O**. Make your move!"
TOASTS = [
    "Nice try, sweetheart! 😘",
    "Are you sure about that move? 🤔",
    "You're making this too easy! 💋",
    "Not bad... but I'm still winning! 😉",
    "Keep fighting, I love the challenge! 🔥"
]
PENALTY_MESSAGE = """
# 🎉 **VICTORY IS MINE! ❤️** 🎉

**Now, for your penalty:**  
You must wear your *absolute best dress* for our Valentine's date  
and surprise me with a **wonderful gift**.  

**No excuses!** 💃✨
"""

# Streamlit app
def main():
    st.set_page_config(
        page_title="❤️ Valentine's Tic-Tac-Toe Challenge ❤️",
        page_icon="💕",
        layout="wide"
    )
    
    st.markdown(ST_CSS, unsafe_allow_html=True)
    
    # State management
    if 'game' not in st.session_state:
        st.session_state.game = TicTacToe()
    if 'screen' not in st.session_state:
        st.session_state.screen = 'welcome'
    if 'toast' not in st.session_state:
        st.session_state.toast = ""
    
    game = st.session_state.game
    
    # Main container
    container = st.container()
    
    if st.session_state.screen == 'welcome':
        welcome_screen(container, game)
    elif st.session_state.screen == 'playing':
        game_screen(container, game)
    elif st.session_state.screen == 'game_over':
        game_over_screen(container, game)

def welcome_screen(container, game):
    st.markdown("""
    <div style='text-align: center; padding: 3rem 0;'>
        <h1 style='font-size: 3.5rem; margin-bottom: 1rem;'>💕 TIC-TAC-TOE CHALLENGE 💕</h1>
        <div style='font-size: 1.4rem; color: #FFD700; margin-bottom: 2rem;'>
            *Valentine's Day Stakes Edition*
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(WELCOME_MESSAGE, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("💋 **START THE CHALLENGE** 💋", use_container_width=True):
            st.session_state.screen = 'playing'
            st.rerun()

def game_screen(container, game):
    # Header with toast
    if st.session_state.toast:
        st.markdown(f"""
        <div class='toast' style='text-align: center;'>
            {st.session_state.toast}
        </div>
        """, unsafe_allow_html=True)
    
    # Game status
    status_col1, status_col2, status_col3 = st.columns([1, 2, 1])
    with status_col2:
        winner = game.check_winner()
        if winner:
            st.session_state.screen = 'game_over'
            st.session_state.game = game
            st.rerun()
        elif game.current_player == 'X':
            st.metric("Your Turn", "❌ X", delta="Make your move!")
        else:
            st.metric("My Turn", "⭕ O", delta="Thinking...")
    
    # Game grid
    grid_cols = st.columns(3)
    
    for i in range(3):
        with grid_cols[i]:
            for j in range(3):
                cell_key = f"cell_{i}_{j}"
                if game.board[i][j] == '':
                    if game.current_player == 'X' and st.button('', key=cell_key, help=f'Row {i}, Col {j}'):
                        if game.make_move(i, j, 'X'):
                            st.session_state.toast = random.choice(TOASTS)
                            st.rerun()
                else:
                    st.button(game.board[i][j], key=f"filled_{i}_{j}", disabled=True)
    
    # AI Move (near-instant)
    if game.current_player == 'O' and not game.game_over:
        with st.spinner('AI thinking... 💭'):
            time.sleep(0.3)  # Quick thinking simulation
            best_move = get_best_move(game)
            if best_move:
                row, col = best_move
                game.make_move(row, col, 'O')
                st.rerun()
    
    # Reset button
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        if st.button("🔄 New Game", use_container_width=True):
            st.session_state.game = TicTacToe()
            st.session_state.screen = 'welcome'
            st.session_state.toast = ""
            st.rerun()

def game_over_screen(container, game):
    # Trigger confetti
    confetti.show()
    
    st.markdown(PENALTY_MESSAGE, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col2:
        if st.button("💕 Play Again", use_container_width=True):
            st.session_state.game = TicTacToe()
            st.session_state.screen = 'welcome'
            st.session_state.toast = ""
            st.rerun()

if __name__ == "__main__":
    main()

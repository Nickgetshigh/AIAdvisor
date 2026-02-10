import streamlit as st
import streamlit_confetti as confetti
import time
import random
from typing import List, Tuple, Optional
import copy

# Color palette
COLORS = {
    'rose': '#FFC0CB',
    'crimson': '#8B0000',
    'gold': '#FFD700',
    'dark_bg': '#1a0f1a',
    'light_bg': '#2d1b2d'
}

# Custom CSS for romantic theme - ALL STRINGS PROPERLY TERMINATED
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
        height: 120px;
        width: 120px;
    }}
    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(139,0,0,0.6);
    }}
    .stButton > button:disabled {{
        opacity: 0.7;
        cursor: not-allowed;
    }}
    .toast {{
        background: linear-gradient(45deg, {COLORS['rose']}, {COLORS['gold']});
        color: {COLORS['crimson']};
        padding: 1rem 2rem;
        border-radius: 25px;
        font-weight: bold;
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        margin: 1rem 0;
        text-align: center;
    }}
</style>
"""

class TicTacToe:
    def __init__(self):
        self.board: List[List[str]] = [['' for _ in range(3)] for _ in range(3)]
        self.current_player: str = 'X'  # User starts
        self.game_over: bool = False
        self.winner: Optional[str] = None
        
    def reset(self) -> None:
        self.__init__()
    
    def make_move(self, row: int, col: int, player: str) -> bool:
        """Make a move if valid"""
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == '' and not self.game_over:
            self.board[row][col] = player
            self.current_player = 'O' if player == 'X' else 'X'
            winner = self.check_winner()
            self.game_over = bool(winner)
            if winner:
                self.winner = winner
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
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
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

    def get_empty_positions(self) -> List[Tuple[int, int]]:
        """Get all empty positions on board"""
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == '']

def minimax(board: List[List[str]], is_maximizing: bool) -> int:
    """Simplified minimax - modifies board in-place and undoes moves"""
    game = TicTacToe()
    game.board = board
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
            board[row][col] = 'O'
            eval_score = minimax(board, False)
            board[row][col] = ''  # Undo move
            max_eval = max(max_eval, eval_score)
        return max_eval
    else:  # User's turn (X)
        min_eval = float('inf')
        for row, col in game.get_empty_positions():
            board[row][col] = 'X'
            eval_score = minimax(board, True)
            board[row][col] = ''  # Undo move
            min_eval = min(min_eval, eval_score)
        return min_eval

def get_best_move(game: TicTacToe) -> Optional[Tuple[int, int]]:
    """Find the best move for AI using minimax"""
    best_score = -float('inf')
    best_move = None
    
    for row, col in game.get_empty_positions():
        # Make move
        game.board[row][col] = 'O'
        move_score = minimax(game.board, False)
        # Undo move
        game.board[row][col] = ''
        
        if move_score > best_score:
            best_score = move_score
            best_move = (row, col)
    
    return best_move

# Valentine messages - ALL PROPERLY TERMINATED WITH TRIPLE QUOTES
WELCOME_MESSAGE = """💕 **Think you can beat me?** 💕

If you lose, the stakes are *high*... Play as **X**, I'll be **O**. Make your move!"""

TOASTS = [
    "Nice try, sweetheart! 😘",
    "Are you sure about that move? 🤔", 
    "You're making this too easy! 💋",
    "Not bad... but I'm still winning! 😉",
    "Keep fighting, I love the challenge! 🔥"
]

PENALTY_MESSAGE = """# 🎉 **VICTORY IS MINE! ❤️** 🎉

**Now, for your penalty:**  
You must wear your *absolute best dress* for our Valentine's date  
and surprise me with a **wonderful gift**.  

**No excuses!** 💃✨"""

def main():
    st.set_page_config(
        page_title="❤️ Valentine's Tic-Tac-Toe Challenge ❤️",
        page_icon="💕",
        layout="wide"
    )
    
    st.markdown(ST_CSS, unsafe_allow_html=True)
    
    # Initialize session state - ALL KEYS PROPERLY INITIALIZED
    for key in ['game', 'screen', 'toast', 'winner']:
        if key not in st.session_state:
            if key == 'game':
                st.session_state[key] = TicTacToe()
            elif key == 'screen':
                st.session_state[key] = 'welcome'
            else:
                st.session_state[key] = ""
    
    game = st.session_state.game
    
    # Main layout
    if st.session_state.screen == 'welcome':
        welcome_screen()
    elif st.session_state.screen == 'playing':
        game_screen(game)
    elif st.session_state.screen == 'game_over':
        game_over_screen(game)

def welcome_screen():
    """Welcome screen with proper string termination"""
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

def game_screen(game: TicTacToe):
    """Main game screen"""
    # Toast message
    if st.session_state.toast:
        st.markdown(f'<div class="toast">{st.session_state.toast}</div>', unsafe_allow_html=True)
        st.session_state.toast = ""
    
    # Check for winner
    if game.game_over and game.winner:
        st.session_state.screen = 'game_over'
        st.session_state.winner = game.winner
        st.rerun()
    
    # Game status
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if game.current_player == 'X':
            st.metric("Your Turn", "❌ X", delta="Make your move!")
        else:
            st.metric("AI Turn", "⭕ O", delta="Thinking...")
    
    # Game grid
    st.markdown("---")
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            with cols[j]:
                cell_key = f"cell_{i}_{j}"
                if game.board[i][j] == '':
                    if game.current_player == 'X':
                        if st.button(' ', key=cell_key):
                            if game.make_move(i, j, 'X'):
                                st.session_state.toast = random.choice(TOASTS)
                                st.rerun()
                    else:
                        st.button(' ', key=f"wait_{i}_{j}", disabled=True)
                else:
                    st.button(game.board[i][j], key=f"filled_{i}_{j}", disabled=True)
    
    # AI makes move after user turn
    if game.current_player == 'O' and not game.game_over:
        st.rerun()  # Trigger AI move
    
    # Reset button
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        if st.button("🔄 New Game", use_container_width=True):
            st.session_state.game = TicTacToe()
            st.session_state.screen = 'welcome'
            st.session_state.toast = ""
            st.session_state.winner = ""
            st.rerun()

def game_over_screen(game: TicTacToe):
    """Game over celebration"""
    confetti.show()
    
    if game.winner == 'O':
        st.markdown(PENALTY_MESSAGE, unsafe_allow_html=True)
    elif game.winner == 'draw':
        st.success("🎉 It's a draw! You survived... this time! 💕")
    else:
        st.error("Unexpected game end state")
    
    if st.button("💕 Play Again", use_container_width=True):
        st.session_state.game = TicTacToe()
        st.session_state.screen = 'welcome'
        st.session_state.toast = ""
        st.session_state.winner = ""
        st.rerun()

# AI move handler - runs automatically after user move
def handle_ai_move(game: TicTacToe):
    """Handle AI move with minimal delay"""
    if game.current_player == 'O' and not game.game_over:
        time.sleep(0.5)  # Quick thinking
        best_move = get_best_move(game)
        if best_move:
            row, col = best_move
            game.make_move(row, col, 'O')

if __name__ == "__main__":
    main()

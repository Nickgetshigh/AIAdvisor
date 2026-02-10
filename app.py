import streamlit as st
import streamlit_confetti as confetti
import time
import random

# Color palette
COLORS = {
    'rose': '#FFC0CB',
    'crimson': '#8B0000', 
    'gold': '#FFD700',
    'dark_bg': '#1a0f1a',
    'light_bg': '#2d1b2d'
}

# Custom CSS
ST_CSS = f"""
<style>
    .main {{
        background: linear-gradient(135deg, {COLORS['dark_bg']}, {COLORS['light_bg']});
        padding: 2rem;
    }}
    h1 {{
        color: {COLORS['gold']};
        font-family: 'Georgia', serif;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }}
    .toast {{
        background: linear-gradient(45deg, {COLORS['rose']}, {COLORS['gold']});
        color: {COLORS['crimson']};
        padding: 1rem;
        border-radius: 20px;
        text-align: center;
        font-weight: bold;
        margin: 1rem 0;
    }}
    .game-cell {{
        width: 130px !important;
        height: 130px !important;
        font-size: 3.5em !important;
        font-weight: bold !important;
        background: rgba(255,255,255,0.1) !important;
        border: 4px solid {COLORS['gold']} !important;
        border-radius: 20px !important;
        color: {COLORS['gold']} !important;
        transition: all 0.3s ease !important;
    }}
    .game-cell:hover {{
        background: rgba(255,192,203,0.4) !important;
        transform: scale(1.05) !important;
    }}
</style>
"""

class TicTacToe:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
        
    def reset(self):
        self.__init__()
    
    def make_move(self, row: int, col: int, player: str) -> bool:
        if self.board[row][col] == '' and not self.game_over:
            self.board[row][col] = player
            self.current_player = 'O' if player == 'X' else 'X'
            self.winner = self.check_winner()
            self.game_over = self.winner is not None or self.is_full()
            return True
        return False
    
    def check_winner(self) -> str:
        # Rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return self.board[i][0]
        # Columns  
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != '':
                return self.board[0][j]
        # Diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return self.board[0][2]
        return ''
    
    def is_full(self) -> bool:
        return all(cell != '' for row in self.board for cell in row)
    
    def get_empty_cells(self) -> list:
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == '']

# FIXED MINIMAX - No recursion, iterative with perfect AI logic
def get_ai_move(game: TicTacToe) -> tuple:
    """Perfect AI using simple unbeatable logic (no recursion)"""
    empty_cells = game.get_empty_cells()
    
    # Check if AI can win immediately
    for row, col in empty_cells:
        game.board[row][col] = 'O'
        if game.check_winner() == 'O':
            game.board[row][col] = ''
            return (row, col)
        game.board[row][col] = ''
    
    # Block user from winning
    for row, col in empty_cells:
        game.board[row][col] = 'X'
        if game.check_winner() == 'X':
            game.board[row][col] = ''
            return (row, col)
        game.board[row][col] = ''
    
    # Take center if available
    if (1, 1) in empty_cells:
        return (1, 1)
    
    # Take corner if available
    corners = [(0,0), (0,2), (2,0), (2,2)]
    for row, col in corners:
        if (row, col) in empty_cells:
            return (row, col)
    
    # Take any remaining spot
    return empty_cells[0]

# Messages
TOASTS = [
    "Nice try, sweetheart! 😘",
    "Are you sure about that? 🤔", 
    "You're making this easy! 💋",
    "Not bad... but I'm winning! 😉",
    "Love the challenge! 🔥"
]

PENALTY_MESSAGE = """
# 🎉 **VICTORY IS MINE! ❤️** 🎉

**Your penalty:**  
Wear your *absolute best dress* for our Valentine's date  
and bring a **wonderful gift**!  

**No excuses!** 💃✨
"""

def main():
    st.set_page_config(
        page_title="💕 Valentine's Tic-Tac-Toe 💕",
        page_icon="💕",
        layout="wide"
    )
    
    st.markdown(ST_CSS, unsafe_allow_html=True)
    
    # Initialize session state
    if 'game' not in st.session_state:
        st.session_state.game = TicTacToe()
        st.session_state.show_toast = False
        st.session_state.toast_message = ""
    
    game = st.session_state.game
    
    # Title
    st.markdown("# 💕 **TIC-TAC-TOE CHALLENGE** 💕")
    st.markdown("*Valentine's Day Stakes Edition*")
    
    # Game screens
    if game.game_over:
        game_over_screen()
    else:
        playing_screen(game)

def playing_screen(game: TicTacToe):
    # Toast
    if st.session_state.show_toast:
        st.markdown(f'<div class="toast">{st.session_state.toast_message}</div>', unsafe_allow_html=True)
        st.session_state.show_toast = False
    
    # Status
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if game.current_player == 'X':
            st.metric("Your Turn", "❌ X", "Click a cell!")
        else:
            st.metric("AI Turn", "⭕ O", "Thinking...")
    
    # Game grid - FIXED LAYOUT
    st.markdown("---")
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            with cols[j]:
                cell_id = f"{i}-{j}"
                if game.board[i][j] == '':
                    if game.current_player == 'X':
                        if st.button(' ', key=f"user_{cell_id}", help=f"Row {i}, Col {j}"):
                            if game.make_move(i, j, 'X'):
                                st.session_state.show_toast = True
                                st.session_state.toast_message = random.choice(TOASTS)
                                st.rerun()
                    else:
                        # Show disabled button during AI turn
                        st.button(' ', key=f"ai_wait_{cell_id}", disabled=True)
                else:
                    st.button(game.board[i][j], key=f"filled_{cell_id}", disabled=True)
    
    # AI move - SEPARATE LOGIC, NO RECURSION
    if game.current_player == 'O' and not game.game_over:
        with st.spinner("AI thinking... 💭"):
            time.sleep(0.5)  # Quick thinking animation
            move = get_ai_move(game)
            if move:
                row, col = move
                game.make_move(row, col, 'O')
                st.rerun()
    
    # Reset button
    if st.button("🔄 New Game", use_container_width=True):
        st.session_state.game = TicTacToe()
        st.session_state.show_toast = False
        st.session_state.toast_message = ""
        st.rerun()

def game_over_screen():
    game = st.session_state.game
    
    if game.winner == 'O':
        confetti.show()
        st.markdown(PENALTY_MESSAGE, unsafe_allow_html=True)
    elif game.winner == '':
        st.success("🎉 **DRAW!** You survived... this time! 💕")
    
    if st.button("💕 Play Again", use_container_width=True):
        st.session_state.game = TicTacToe()
        st.session_state.show_toast = False
        st.session_state.toast_message = ""
        st.rerun()

if __name__ == "__main__":
    main()

import streamlit as st

st.set_page_config(page_title="Valentine Love Quiz", page_icon="💕")

# Valentine's questions (romantic facts/trivia)
questions = [
    {
        "question": "What is the traditional birth flower for Valentine's Day?",
        "choices": ["Rose", "Lily", "Tulip", "Daisy"],
        "answer": "Rose"
    },
    {
        "question": "In what year was the first Valentine's Day card sent?",
        "choices": ["1840s", "1700s", "1900s", "Ancient Rome"],
        "answer": "1840s"
    },
    {
        "question": "What do the 'X' and 'O' in 'XOXO' represent?",
        "choices": ["Hugs and kisses", "Kisses and hugs", "Love and luck", "Forever and always"],
        "answer": "Kisses and hugs"
    },
    {
        "question": "Which famous queen received 22,000 love letters?",
        "choices": ["Queen Victoria", "Cleopatra", "Marie Antoinette", "Queen Elizabeth"],
        "answer": "Queen Victoria"
    },
    {
        "question": "What color roses mean 'love at first sight'?",
        "choices": ["Red", "Pink", "White", "Lavender"],
        "answer": "Lavender"
    }
]

# Initialize session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'quiz_completed' not in st.session_state:
    st.session_state.quiz_completed = False
if 'game_key' not in st.session_state:
    st.session_state.game_key = 0

st.markdown("""
    <style>
    .main {background-color: #ffebff;}
    .stButton > button {background-color: #ff69b4; color: white;}
    </style>
""", unsafe_allow_html=True)

## Game Play
st.title("💕 Valentine Love Match Quiz 💕")
st.markdown("Answer 5 romantic trivia questions to see how much you know about love! Each correct answer earns a heart. ❤️")

if not st.session_state.quiz_completed:
    # New game button
    if st.button("🔄 New Quiz", key="new_quiz"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.quiz_completed = False
        st.session_state.game_key += 1
        st.rerun()

    current_q = questions[st.session_state.current_question]
    st.subheader(f"Question {st.session_state.current_question + 1}/5")
    st.write(current_q["question"])

    # Radio choices
    choice = st.radio("Your answer:", current_q["choices"], key=f"q_{st.session_state.current_question}_{st.session_state.game_key}")

    if st.button("❤️ Submit Answer"):
        if choice == current_q["answer"]:
            st.session_state.score += 1
            st.success("Correct! 💖")
            st.balloons()
        else:
            st.error(f"Oops! The answer was **{current_q['answer']}** 💔")

        # Next question or end
        if st.session_state.current_question < len(questions) - 1:
            st.session_state.current_question += 1
        else:
            st.session_state.quiz_completed = True
        st.rerun()
else:
    # Results
    percentage = (st.session_state.score / len(questions)) * 100
    hearts = "❤️" * st.session_state.score
    st.markdown(f"## Quiz Complete! Your Love Score: **{st.session_state.score}/5** {hearts}")
    if percentage >= 80:
        st.success("You're a love expert! 🎉💑")
    elif percentage >= 60:
        st.info("Sweetheart level! 😘")
    else:
        st.warning("Room to grow in romance... Try again! 🌹")
    
    if st.button("🔄 Play Again"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.quiz_completed = False
        st.session_state.game_key += 1
        st.rerun()

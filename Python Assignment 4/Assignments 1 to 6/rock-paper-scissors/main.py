import streamlit as st
import random

# Emojis for visuals
emoji_map = {
    'Rock': '✊',
    'Paper': '✋',
    'Scissors': '✌'
}

options = ['Rock', 'Paper', 'Scissors']

# Session state for score tracking
if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
if 'computer_score' not in st.session_state:
    st.session_state.computer_score = 0

st.title("Rock ✊ Paper ✋ Scissors ✌")
st.subheader("Can you beat the computer?")

# Scoreboard
col1, col2 = st.columns(2)
col1.metric("Your Score", st.session_state.user_score)
col2.metric("Computer Score", st.session_state.computer_score)

# Game input
user_choice = st.radio("Pick your move:", options, horizontal=True)

if st.button("Play"):
    computer_choice = random.choice(options)
    st.write(f"*You chose:* {emoji_map[user_choice]} {user_choice}")
    st.write(f"*Computer chose:* {emoji_map[computer_choice]} {computer_choice}")

    if user_choice == computer_choice:
        st.info("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        st.success("You win this round!")
        st.session_state.user_score += 1
    else:
        st.error("Computer wins this round!")
        st.session_state.computer_score += 1

if st.button("Reset Game"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.success("Scores have been reset!")

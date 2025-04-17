import streamlit as st
import random

# Title
st.title("Guess the Number Game")

# Initialize the number to guess in session state
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# Instructions
st.write("I'm thinking of a number between *1 and 100*. Can you guess it?")

# User input
if not st.session_state.game_over:
    guess = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if guess == st.session_state.number:
            st.success(f"Correct! The number was {st.session_state.number}.")
            st.balloons()
            st.write(f"You guessed it in {st.session_state.attempts} attempts.")
            st.session_state.game_over = True
        elif guess < st.session_state.number:
            st.info("Too low! Try a higher number.")
        else:
            st.info("Too high! Try a lower number.")
else:
    if st.button("Play Again"):
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = True

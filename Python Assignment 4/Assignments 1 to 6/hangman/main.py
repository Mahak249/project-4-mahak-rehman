import streamlit as st
import random

# List of words to guess
word_list = ['apple', 'banana', 'computer', 'streamlit', 'python', 'laptop', 'flower']

# Initialize session state
if 'word' not in st.session_state:
    st.session_state.word = random.choice(word_list)
    st.session_state.display_word = ['_'] * len(st.session_state.word)
    st.session_state.guessed_letters = []
    st.session_state.attempts_left = 6
    st.session_state.game_over = False

# Title
st.title("Hangman Game")

# Display current word state
st.subheader("Word:")
st.write(' '.join(st.session_state.display_word))
st.write(f"Attempts left: {st.session_state.attempts_left}")
st.write(f"Guessed letters: {', '.join(st.session_state.guessed_letters)}")

# Game input
if not st.session_state.game_over:
    guess = st.text_input("Enter a letter: ").lower()

    if st.button("Submit Guess"):
        if guess and guess.isalpha() and len(guess) == 1:
            if guess in st.session_state.guessed_letters:
                st.warning("You already guessed that letter.")
            else:
                st.session_state.guessed_letters.append(guess)
                if guess in st.session_state.word:
                    for i, letter in enumerate(st.session_state.word):
                        if letter == guess:
                            st.session_state.display_word[i] = guess
                    if '_' not in st.session_state.display_word:
                        st.success(f"Congratulations! You guessed the word: {st.session_state.word}")
                        st.balloons()
                        st.session_state.game_over = True
                else:
                    st.session_state.attempts_left -= 1
                    if st.session_state.attempts_left == 0:
                        st.error(f"Game Over! The word was: {st.session_state.word}")
                        st.session_state.game_over = True
        else:
            st.warning("Please enter a single letter.")

else:
    if st.button("Play Again"):
        st.session_state.word = random.choice(word_list)
        st.session_state.display_word = ['_'] * len(st.session_state.word)
        st.session_state.guessed_letters = []
        st.session_state.attempts_left = 6
        st.session_state.game_over = True

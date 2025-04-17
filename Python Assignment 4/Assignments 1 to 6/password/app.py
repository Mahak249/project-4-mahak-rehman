import streamlit as st
import random
import string
from password_strength import PasswordStats  # type: ignore

# Function to generate password
def generate_password(length, use_uppercase, use_digits, use_special):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

# Function to check password strength
def check_password_strength(password):
    stats = PasswordStats(password)
    strength = stats.strength()

    if strength < 0.3:
        return "Weak", "#FF4C4C"  # Red
    elif strength < 0.6:
        return "Medium", "#FFA500"  # Orange
    else:
        return "Strong", "#32CD32"  # Green

# Streamlit UI Customization
st.set_page_config(page_title="Stylish Password Generator", layout="centered")

st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #141E30, #243B55);
            color: white;
            font-family: Arial, sans-serif;
        }
        .big-font {
            font-size:25px !important;
            font-weight: bold;
            text-align: center;
        }
        .password-box {
            background: #2C3E50;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: #1ABC9C;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='big-font'>✨ Stylish Password Generator ✨</h1>", unsafe_allow_html=True)

# Sidebar Customization Options
st.sidebar.header("⚙ Customize Your Password")
length = st.sidebar.slider("Password Length:", min_value=6, max_value=30, value=12)
use_uppercase = st.sidebar.checkbox("Include Uppercase Letters")
use_digits = st.sidebar.checkbox("Include Numbers")
use_special = st.sidebar.checkbox("Include Special Characters")

# Generate password on button click
if st.sidebar.button("🔄 Generate Password"):
    password = generate_password(length, use_uppercase, use_digits, use_special)
    st.session_state["password"] = password

# Get the generated password from session state
password = st.session_state.get("password", "")

if password:
    st.markdown("<div class='password-box'>{}</div>".format(password), unsafe_allow_html=True)

    # Strength meter
    strength, color = check_password_strength(password)
    st.markdown(f"<h3 style='color: {color}; text-align: center;'>Strength: {strength}</h3>", unsafe_allow_html=True)
    st.progress({"Weak": 0.3, "Medium": 0.6, "Strong": 1.0}[strength])

    # Toggle password visibility
    show_password = st.checkbox("👀 Show Password")
    if show_password:
        st.text_input("Your Password:", value=password, disabled=True)

st.caption("Built with ❤ using Streamlit")

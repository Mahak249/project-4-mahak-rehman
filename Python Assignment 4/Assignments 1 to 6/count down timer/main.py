import streamlit as st
import time

st.title("Countdown Timer")

# User input for countdown time
minutes = st.number_input("Enter minutes", min_value=0, max_value=60, step=1)
seconds = st.number_input("Enter seconds", min_value=0, max_value=59, step=1)

# Convert total time to seconds
total_seconds = int(minutes * 60 + seconds)

if st.button("Start Countdown"):
    if total_seconds > 0:
        st.write("Timer Started!")
        countdown_placeholder = st.empty()

        for i in range(total_seconds, -1, -1):
            mins, secs = divmod(i, 60)
            countdown_placeholder.markdown(f"### {mins:02d}:{secs:02d}")
            time.sleep(1)

        st.balloons()
        st.success("Time's up!")
    else:
        st.warning("Please enter a time greater than 0.")

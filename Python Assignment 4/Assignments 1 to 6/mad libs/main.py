import streamlit as st

st.title("Mad Libs Generator")

st.write("Fill in the blanks below to generate your funny story!")

# Input fields
noun = st.text_input("Enter a noun:")
verb = st.text_input("Enter a verb:")
adjective = st.text_input("Enter an adjective:")
place = st.text_input("Enter a place:")
animal = st.text_input("Enter an animal:")

if st.button("Generate Story"):
    if noun and verb and adjective and place and animal:
        story = f"""
        Once upon a time in {place}, there was a very {adjective} {animal}.
        It loved to {verb} every day with its favorite {noun}.
        People from all around the world came to {place} to see the amazing {animal} in action.
        The end.
        """
        st.subheader("Here's your Mad Libs story:")
        st.write(story)
    else:
        st.warning("Please fill in all fields to generate the story.")

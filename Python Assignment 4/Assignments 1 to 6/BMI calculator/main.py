import streamlit as st

# Title
st.title("BMI Calculator")

# User inputs
st.subheader("Enter your details:")
weight = st.number_input("Weight (kg)", min_value=1.0, format="%.2f")
height = st.number_input("Height (cm)", min_value=1.0, format="%.2f")

# Calculate BMI
if st.button("Calculate BMI"):
    if weight and height:
        height_m = height / 100  # convert cm to meters
        bmi = weight / (height_m ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")

        # BMI Category
        if bmi < 18.5:
            st.warning("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.info("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.warning("Please enter valid weight and height.")

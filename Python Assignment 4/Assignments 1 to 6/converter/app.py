import streamlit as st

def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "m": 1, "km": 0.001, "cm": 100, "mm": 1000
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def weight_converter(value, from_unit, to_unit):
    conversion_factors = {
        "g": 1, "kg": 0.001, "mg": 1000
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def volume_converter(value, from_unit, to_unit):
    conversion_factors = {
        "L": 1, "mL": 1000, "m³": 0.001
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

# Custom Styling
st.markdown(
    """
    <style>
        body { background-color: #f8f9fa; color: #333333; }
        .stButton button {
            background: linear-gradient(90deg, #ff8a00, #da1b60);
            color: white;
            padding: 12px;
            border-radius: 25px;
            font-weight: bold;
            border: none;
            box-shadow: 0px 4px 10px rgba(255, 138, 0, 0.3);
            transition: transform 0.2s ease;
        }
        .stButton button:hover {
            transform: scale(1.05);
            box-shadow: 0px 6px 15px rgba(255, 138, 0, 0.5);
            color:black;
        }
        .stSelectbox, .stTextInput, .stNumberInput {
            border-radius: 15px;
            padding: 10px;
            background-color: #ffffff;
            color: #333333;
            border: 1px solid #ff8a00;
        }
        .stSidebar {
            background-color: #ffebd6;
            padding: 15px;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("🌟 Elegant Unit Converter")
choice = st.sidebar.radio("Select Conversion Type:", ["Length", "Weight", "Volume"])

st.title("✨ Advanced Unit Converter")
value = st.number_input("Enter Value:", min_value=0.0, step=0.1)

if choice == "Length":
    from_unit = st.selectbox("From Unit:", ["m", "km", "cm", "mm"])
    to_unit = st.selectbox("To Unit:", ["m", "km", "cm", "mm"])
    if st.button("🚀 Convert Now!"):
        result = length_converter(value, from_unit, to_unit)
        st.success(f"🎯 Converted Value: {result:.4f} {to_unit}")

elif choice == "Weight":
    from_unit = st.selectbox("From Unit:", ["g", "kg", "mg"])
    to_unit = st.selectbox("To Unit:", ["g", "kg", "mg"])
    if st.button("⚖ Convert Now!"):
        result = weight_converter(value, from_unit, to_unit)
        st.success(f"🎯 Converted Value: {result:.4f} {to_unit}")

elif choice == "Volume":
    from_unit = st.selectbox("From Unit:", ["L", "mL", "m³"])
    to_unit = st.selectbox("To Unit:", ["L", "mL", "m³"])
    if st.button("💧 Convert Now!"):
        result = volume_converter(value, from_unit, to_unit)
        st.success(f"🎯 Converted Value: {result:.4f} {to_unit}")

import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Calculator App",
    page_icon="🧮",
    layout="centered"
)

# Title
st.title("🧮 Advanced Calculator")
st.markdown("Perform basic mathematical operations easily.")

# Functions
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "❌ Division by Zero"
    return a / b

def power(a, b):
    return a ** b

def floor_division(a, b):
    if b == 0:
        return "❌ Division by Zero"
    return a // b


# Sidebar
st.sidebar.header("⚙️ Calculator Menu")

operation = st.sidebar.selectbox(
    "Select Operation",
    [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Power",
        "Floor Division"
    ]
)

# User Inputs
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input(
        "Enter First Number",
        value=0.0,
        format="%.2f"
    )

with col2:
    num2 = st.number_input(
        "Enter Second Number",
        value=0.0,
        format="%.2f"
    )

# Calculate Button
if st.button("Calculate", use_container_width=True):

    if operation == "Addition":
        result = addition(num1, num2)

    elif operation == "Subtraction":
        result = subtraction(num1, num2)

    elif operation == "Multiplication":
        result = multiplication(num1, num2)

    elif operation == "Division":
        result = division(num1, num2)

    elif operation == "Power":
        result = power(num1, num2)

    elif operation == "Floor Division":
        result = floor_division(num1, num2)

    st.success(f"✅ Result: {result}")

# Footer
st.markdown("---")
st.markdown(
    "<center>Developed using Streamlit 🚀</center>",
    unsafe_allow_html=True
)
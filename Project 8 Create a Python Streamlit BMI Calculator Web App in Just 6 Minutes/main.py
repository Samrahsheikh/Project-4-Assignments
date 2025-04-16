import streamlit as st

# BMI Calculator
st.title("BMI Calculator")

# Taking input for height and weight with unique keys
height = st.number_input("Enter your height (in cm)", min_value=1.0, step=0.1, key="height")
weight = st.number_input("Enter your weight (in kg)", min_value=1.0, step=0.1, key="weight")

# Button to calculate BMI
if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        # Convert height from cm to meters
        height_in_meters = height / 100
        bmi = weight / (height_in_meters ** 2)
        
        st.write(f"Your BMI is: {bmi:.2f}")

        # BMI Category
        if bmi < 18.5:
            st.write("Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            st.write("Category: Normal weight")
        elif 25 <= bmi < 29.9:
            st.write("Category: Overweight")
        else:
            st.write("Category: Obesity")
    else:
        st.write("Please enter valid height and weight values.")

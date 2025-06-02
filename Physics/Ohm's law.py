import streamlit as st

def run():
    st.header("Ohm's Law")

    st.markdown("""
    Ohm's law states the relationship between voltage, current, and resistance:

    \[
    V = I \times R
    \]

    where:
    - \(V\) = voltage (Volts)
    - \(I\) = current (Amperes)
    - \(R\) = resistance (Ohms)
    """)

    st.write("Provide any two values and leave the third as zero to calculate it.")

    V = st.number_input("Voltage (V):", value=0.0)
    I = st.number_input("Current (I) in Amperes:", value=0.0)
    R = st.number_input("Resistance (R) in Ohms:", value=0.0)

    # Calculate the missing value
    try:
        if V == 0 and I != 0 and R != 0:
            V = I * R
            st.success(f"Voltage (V) = {V:.2f} Volts")
        elif I == 0 and V != 0 and R != 0:
            I = V / R
            st.success(f"Current (I) = {I:.2f} Amperes")
        elif R == 0 and V != 0 and I != 0:
            R = V / I
            st.success(f"Resistance (R) = {R:.2f} Ohms")
        else:
            st.info("Please leave exactly one field as zero to calculate it.")
    except ZeroDivisionError:
        st.error("Division by zero error. Please enter valid inputs.")

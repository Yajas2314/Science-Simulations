import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.header("Projectile Motion")

    st.markdown("""
    Projectile motion describes the motion of an object thrown into the air, subject to gravity.

    Key formulas:
    - Horizontal range: \( R = \frac{v_0^2 \sin 2\theta}{g} \)
    - Maximum height: \( H = \frac{v_0^2 \sin^2 \theta}{2g} \)
    - Time of flight: \( T = \frac{2 v_0 \sin \theta}{g} \)

    where:
    - \(v_0\) = initial velocity (m/s)
    - \(\theta\) = launch angle (degrees)
    - \(g = 9.8\, m/s^2\) (acceleration due to gravity)
    """)

    v0 = st.number_input("Initial velocity \(v_0\) (m/s):", min_value=0.0, value=20.0)
    angle_deg = st.slider("Launch angle \(\theta\) (degrees):", 0, 90, 45)

    g = 9.8
    theta = np.radians(angle_deg)

    # Calculate time of flight, max height, and range
    T = 2 * v0 * np.sin(theta) / g
    H = (v0 ** 2) * (np.sin(theta) ** 2) / (2 * g)
    R = (v0 ** 2) * np.sin(2 * theta) / g

    st.write(f"Time of flight: {T:.2f} seconds")
    st.write(f"Maximum height: {H:.2f} meters")
    st.write(f"Horizontal Range: {R: .2f} metres")

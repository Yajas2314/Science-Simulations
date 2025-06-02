import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.header("Wave Optics")

    st.markdown("""
    Wave optics deals with phenomena like interference, diffraction, and polarization.

    Key formulas:

    - Constructive interference occurs at path difference $n \\lambda$
    - Destructive interference occurs at path difference $\\left(n + \\frac{1}{2}\\right) \\lambda$
    - Diffraction angle $\\theta = \\frac{\\lambda}{d}$, where $d$ is slit width
    """)

    wavelength = st.slider("Wavelength (nm):", 380, 750, 600)
    slit_width = st.number_input("Slit width (micrometers):", value=10.0, step=0.1)
    n_order = st.slider("Interference order (n):", 0, 10, 1)

    # Convert inputs to meters
    λ = wavelength * 1e-9
    d = slit_width * 1e-6

    # Calculate angles for constructive and destructive interference
    try:
        theta_constructive = np.degrees(np.arcsin(n_order * λ / d))
    except:
        theta_constructive = None
    try:
        theta_destructive = np.degrees(np.arcsin((n_order + 0.5) * λ / d))
    except:
        theta_destructive = None

    st.write(f"Constructive interference angle (order {n_order}): " +
             (f"{theta_constructive:.2f}°" if theta_constructive and abs(theta_constructive) <= 90 else "Not possible"))
    st.write(f"Destructive interference angle (order {n_order}): " +
             (f"{theta_destructive:.2f}°" if theta_destructive and abs(theta_destructive) <= 90 else "Not possible"))

    # Diffraction angle
    theta_diffraction = np.degrees(λ / d)
    st.write(f"Diffraction angle θ ≈ {theta_diffraction:.2f}°")

    # Plot interference pattern intensity (simplified)
    x =

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.header("🌊 Interference of Light - Wave Optics")

    st.markdown("""
    ## 🔬 Concept
    Interference occurs when two coherent light waves superpose to form a resultant intensity pattern.
    
    **Constructive Interference:**
    \[ I = 4I_0 \cos^2\left(\frac{\Delta\phi}{2}\right) \]
    
    **Destructive Interference:**
    \[ I = 0 \text{ when } \Delta\phi = (2n+1)\pi \]
    """)

    wavelength = st.slider("Wavelength (nm)", 400, 700, 600)
    slit_distance = st.slider("Slit Separation d (μm)", 10, 100, 30)
    screen_distance = st.slider("Screen Distance D (cm)", 10, 100, 50)

    wavelength *= 1e-9
    d = slit_distance * 1e-6
    D = screen_distance * 1e-2

    x = np.linspace(-0.01, 0.01, 1000)
    beta = (2 * np.pi * d * x) / (wavelength * D)
    I = 4 * (np.cos(beta / 2))**2

    fig, ax = plt.subplots()
    ax.plot(x * 1000, I, 'purple')
    ax.set_xlabel("Screen Position x (mm)")
    ax.set_ylabel("Intensity")
    ax.set_title("Double Slit Interference Pattern")
    ax.grid(True)
    st.pyplot(fig)

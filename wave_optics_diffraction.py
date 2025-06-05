import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.header("🌈 Diffraction of Light - Wave Optics")

    st.markdown("""
    ## 🔬 Concept
    Diffraction is the bending of light around obstacles or edges.
    
    **Single Slit Diffraction Intensity:**
    \[ I(\theta) = I_0 \left(\frac{\sin(\beta)}{\beta}\right)^2 \quad \text{where } \beta = \frac{\pi a \sin(\theta)}{\lambda} \]
    """)

    wavelength = st.slider("Wavelength (nm)", 400, 700, 600)
    slit_width = st.slider("Slit Width a (μm)", 10, 100, 30)

    wavelength *= 1e-9
    a = slit_width * 1e-6
    theta = np.linspace(-0.02, 0.02, 1000)
    beta = (np.pi * a * np.sin(theta)) / wavelength

    I = (np.sinc(beta / np.pi))**2

    fig, ax = plt.subplots()
    ax.plot(np.degrees(theta), I, 'darkblue')
    ax.set_xlabel("Angle (degrees)")
    ax.set_ylabel("Normalized Intensity")
    ax.set_title("Single Slit Diffraction Pattern")
    ax.grid(True)
    st.pyplot(fig)

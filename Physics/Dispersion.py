import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.header("Dispersion of Light")

    st.markdown("""
    Dispersion is the splitting of white light into its constituent colors (spectrum) because the refractive index varies with wavelength.

    The speed of light in a medium is:

    $$ v = \frac{c}{n} $$

    where:
    - $c$ = speed of light in vacuum
    - $n$ = refractive index (depends on wavelength)
    """)

    wavelength = st.slider("Select wavelength (nm)", 380, 750, 550)

    # Approximate refractive index for glass as function of wavelength
    # Simplified Cauchy's equation n(λ) = A + B/(λ^2), A=1.5, B=5000 (approx)
    A = 1.5
    B = 5000
    n = A + B / (wavelength ** 2)

    c = 3e8  # speed of light in m/s
    v = c / n

    st.write(f"Refractive index at {wavelength} nm is approximately {n:.4f}")
    st.write(f"Speed of light in medium = {v:.2e} m/s")

    # Show simple spectrum diagram
    fig, ax = plt.subplots(figsize=(8, 1))
    colors = ['violet', 'blue', 'cyan', 'green', 'yellow', 'orange', 'red']
    wavelengths = np.linspace(380, 750, 7)
    for i, wl in enumerate(wavelengths):
        ax.axvspan(wl, wl+50, color=colors[i], alpha=0.6)
        ax.text(wl+20, 0.5, colors[i].capitalize(), rotation=90, va='center')

    ax.set_xlim(380, 800)
    ax.set_ylim(0, 1)
    ax.axis('off')
    st.pyplot(fig)

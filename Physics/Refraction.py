import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.header("Refraction of Light")

    st.markdown("""
    When light passes from one medium to another, it bends according to Snell's Law:

    $$ n_1 \sin \\theta_1 = n_2 \sin \\theta_2 $$

    where:
    - $n_1, n_2$: refractive indices of the media
    - $\\theta_1$: angle of incidence
    - $\\theta_2$: angle of refraction
    """)

    n1 = st.number_input("Refractive index of medium 1 (n₁):", value=1.0, min_value=1.0)
    n2 = st.number_input("Refractive index of medium 2 (n₂):", value=1.33, min_value=1.0)
    angle_incidence = st.slider("Angle of incidence (degrees):", 0, 90, 45)

    # Calculate angle of refraction using Snell's law
    try:
        sin_theta2 = (n1 / n2) * np.sin(np.radians(angle_incidence))
        if sin_theta2 > 1:
            st.warning("Total internal reflection occurs, no refraction.")
            return
        angle_refraction = np.degrees(np.arcsin(sin_theta2))
        st.write(f"Angle of refraction = {angle_refraction:.2f}°")
    except Exception as e:
        st.error("Error in calculation.")

    # Diagram
    fig, ax = plt.subplots(figsize=(6, 5))

    # Boundary between media
    ax.plot([-4, 4], [0, 0], 'k-', lw=4, label="Boundary")

    # Incident ray in medium 1 (above)
    x_inc = [-3, 0]
    y_inc = [3 * np.tan(np.radians(angle_incidence)), 0]
    ax.plot(x_inc, y_inc, 'r-', lw=2, label="Incident Ray")

    # Normal line
    ax.plot([0, 0], [-3, 3], 'b--', lw=1, label="Normal")

    # Refracted ray in medium 2 (below)
    if sin_theta2 <= 1:
        x_ref = [0, 3 * np.sin(np.radians(angle_refraction))]
        y_ref = [0, -3 * np.cos(np.radians(angle_refraction))]
        ax.plot(x_ref, y_ref, 'g-', lw=2, label="Refracted Ray")

    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.axis('off')
    ax.legend()
    st.pyplot(fig)

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.header("Reflection of Light")

    st.markdown("""
    When light hits a plane mirror, it reflects such that the angle of incidence equals the angle of reflection.

    **Law of Reflection:**
    - Angle of incidence = Angle of reflection
    """)

    # Interactive: User inputs angle of incidence
    angle_incidence = st.slider("Select angle of incidence (degrees):", 0, 90, 45)

    # Calculate angle of reflection
    angle_reflection = angle_incidence

    # Show result
    st.write(f"Angle of reflection = {angle_reflection}°")

    # Draw diagram
    fig, ax = plt.subplots(figsize=(5, 5))

    # Mirror line
    ax.plot([0, 0], [0, 4], 'k-', lw=4, label="Mirror")

    # Incident ray
    x_inc = [0, -3 * np.cos(np.radians(angle_incidence))]
    y_inc = [1, 1 + 3 * np.sin(np.radians(angle_incidence))]
    ax.plot(x_inc, y_inc, 'r-', lw=2, label="Incident Ray")

    # Normal line
    ax.plot([0, 0], [0, 4], 'b--', lw=1, label="Normal")

    # Reflected ray
    x_ref = [0, 3 * np.cos(np.radians(angle_reflection))]
    y_ref = [1, 1 + 3 * np.sin(np.radians(angle_reflection))]
    ax.plot(x_ref, y_ref, 'g-', lw=2, label="Reflected Ray")

    ax.set_xlim(-4, 4)
    ax.set_ylim(0, 4)
    ax.axis('off')
    ax.legend()
    st.pyplot(fig)

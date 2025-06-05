import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.header("🚀 Projectile Motion Simulation")

    v0 = st.slider("Initial velocity (m/s)", 1, 100, 30)
    theta = st.slider("Launch angle (degrees)", 0, 90, 45)
    g = 9.8  # gravity

    # Convert angle to radians
    theta_rad = np.radians(theta)

    # Time of flight
    t_flight = 2 * v0 * np.sin(theta_rad) / g

    # Time points
    t = np.linspace(0, t_flight, num=500)

    # X and Y positions
    x = v0 * np.cos(theta_rad) * t
    y = v0 * np.sin(theta_rad) * t - 0.5 * g * t**2

    # Plot trajectory
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel("Horizontal distance (m)")
    ax.set_ylabel("Vertical height (m)")
    ax.set_title(f"Projectile motion: v0={v0} m/s, θ={theta}°")
    ax.grid(True)
    ax.set_ylim(bottom=0)
    st.pyplot(fig)

    # Show key values
    st.markdown(f"**Time of flight:** {t_flight:.2f} s")
    st.markdown(f"**Maximum height:** {(v0**2) * (np.sin(theta_rad))**2 / (2*g):.2f} m")
    st.markdown(f"**Horizontal range:** {(v0**2) * np.sin(2*theta_rad) / g:.2f} m")

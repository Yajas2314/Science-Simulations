import streamlit as st
import numpy as np

def run():
    st.header("Electrostatics")

    st.markdown("""
    Electrostatics deals with electric charges at rest.

    **Key formulas:**
    - Coulomb's law: \( F = k \frac{q_1 q_2}{r^2} \)
    - Electric field: \( E = \frac{F}{q} = k \frac{Q}{r^2} \)
    - Electric potential: \( V = k \frac{Q}{r} \)

    where:
    - \( k = 9 \times 10^9 \, \text{Nm}^2/\text{C}^2 \)
    - \( q_1, q_2, Q \) = charges (Coulombs)
    - \( r \) = distance between charges (meters)
    """)

    k = 9e9
    q1 = st.number_input("Charge q₁ (Coulombs):", value=1e-6, format="%.6e")
    q2 = st.number_input("Charge q₂ (Coulombs):", value=1e-6, format="%.6e")
    r = st.number_input("Distance between charges r (meters):", min_value=0.0001, value=0.1)

    F = k * q1 * q2 / r**2
    E = k * q1 / r**2
    V = k * q1 / r

    st.write(f"Force between charges (F): {F:.4e} N")
    st.write(f"Electric field due to q₁ at distance r (E): {E:.4e} N/C")
    st.write(f"Electric potential due to q₁ at distance r (V): {V:.4e} V")

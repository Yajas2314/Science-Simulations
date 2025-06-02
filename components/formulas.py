formulas = {
    # Physics Formulas
    "Reflection": [
        r"\text{Angle of Incidence} = \text{Angle of Reflection}"
    ],
    "Refraction": [
        r"n_1 \sin \theta_1 = n_2 \sin \theta_2",
        r"n = \frac{c}{v}"
    ],
    "Dispersion": [
        r"v = \frac{c}{n}",
        r"\text{Deviation depends on wavelength}"
    ],
    "Wave Optics": [
        r"\text{Path Difference} = n\lambda \quad (\text{Constructive interference})",
        r"\text{Path Difference} = \left(n + \frac{1}{2}\right) \lambda \quad (\text{Destructive interference})",
        r"\theta = \frac{\lambda}{d}"
    ],
    "Electrostatics": [
        r"F = k \frac{q_1 q_2}{r^2}",
        r"E = \frac{F}{q}",
        r"V = \frac{kq}{r}"
    ],
    "Ohm's Law": [
        r"V = IR",
        r"I = \frac{V}{R}",
        r"R = \frac{V}{I}"
    ],
    "Projectile Motion": [
        r"R = \frac{u^2 \sin 2\theta}{g}",
        r"H = \frac{u^2 \sin^2 \theta}{2g}",
        r"T = \frac{2u \sin \theta}{g}"
    ],

    # Chemistry Formulas
    chemistry_formulas = {
    "Atomic Structure": [
        r"Z = \text{Atomic Number}",
        r"A = \text{Mass Number} = Z + N",
        r"E_n = -13.6 \frac{Z^2}{n^2} \text{ eV}"
    ],
    "Chemical Bonding": [
        r"\text{Ionic Bonding: } \text{Na} + \text{Cl} \to \text{Na}^+ + \text{Cl}^-",
        r"\text{Covalent Bonding: } \text{H} + \text{H} \to \text{H}_2"

}

import streamlit as st
def display_formulas(topic):
    st.subheader("📘 Important Formulas and Equations")
    if topic in formulas:
        for f in formulas[topic]:
            st.latex(f)
    else:
        st.write("No formulas available for this topic.")

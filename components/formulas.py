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
    "Inorganic": [
        r"2H_2 + O_2 \rightarrow 2H_2O",
        r"Fe_2O_3 + 3CO \rightarrow 2Fe + 3CO_2",
        r"CuSO_4 + Zn \rightarrow ZnSO_4 + Cu"
    ],
    "Organic": [
        r"CH_3CH_2OH + O_2 \rightarrow CH_3CHO + H_2O",
        r"C_2H_4 + Br_2 \rightarrow C_2H_4Br_2"
    ],
    "Chemistry Simulations": [
        r"pH = -\log[H^+]",
        r"\text{Indicator color changes with pH}"
    ]
}

import streamlit as st
def display_formulas(topic):
    st.subheader("📘 Important Formulas and Equations")
    if topic in formulas:
        for f in formulas[topic]:
            st.latex(f)
    else:
        st.write("No formulas available for this topic.")

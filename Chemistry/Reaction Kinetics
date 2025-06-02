def run():
    import streamlit as st
    from components.formulas import display_formulas

    st.header("Reaction Kinetics")
    st.markdown("""
    Reaction kinetics studies the speed of chemical reactions and factors affecting it.
    
    **Key Concepts:**
    - Rate law: Rate = k [A]^m [B]^n
    - Order of reaction: sum of m and n
    - Activation energy (Ea)
    """)

    formulas = [
        r"\text{Rate} = k[A]^m[B]^n",
        r"k = A e^{-\frac{E_a}{RT}} \text{ (Arrhenius Equation)}"
    ]
    for f in formulas:
        st.latex(f)

    st.markdown("---")
    st.markdown("### Calculate Rate Constant using Arrhenius Equation")

    import math

    pre_exp_factor = st.number_input("Pre-exponential factor A (s⁻¹)", value=1e12, format="%.2e")
    activation_energy = st.number_input("Activation Energy Ea (kJ/mol)", value=50.0)
    temperature = st.number_input("Temperature T (K)", value=298.0)

    R = 8.314 / 1000  # Gas constant in kJ/mol·K

    k = pre_exp_factor * math.exp(-activation_energy / (R * temperature))
    st.success(f"Rate constant k = {k:.3e} s⁻¹")

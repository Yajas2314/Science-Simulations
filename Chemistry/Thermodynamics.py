def run():
    import streamlit as st
    from components.formulas import display_formulas

    st.header("Thermodynamics")
    st.markdown("""
    Thermodynamics studies energy changes in chemical reactions.
    
    **Key Concepts:**
    - Enthalpy (ΔH)
    - Entropy (ΔS)
    - Gibbs Free Energy (ΔG)
    
    Reaction spontaneity depends on ΔG.
    """)

    formulas = [
        r"\Delta G = \Delta H - T \Delta S",
        r"\text{If } \Delta G < 0, \text{ reaction is spontaneous}"
    ]
    for f in formulas:
        st.latex(f)

    st.markdown("---")
    st.markdown("### Calculate Gibbs Free Energy")

    delta_h = st.number_input("Enthalpy Change ΔH (kJ/mol)", value=0.0)
    delta_s = st.number_input("Entropy Change ΔS (J/mol·K)", value=0.0)
    temperature = st.number_input("Temperature T (K)", value=298.0)

    # Convert ΔS from J to kJ for unit consistency
    delta_s_kj = delta_s / 1000

    delta_g = delta_h - temperature * delta_s_kj
    st.success(f"Gibbs Free Energy ΔG = {delta_g:.3f} kJ/mol")

    if delta_g < 0:
        st.write("Reaction is spontaneous.")
    elif delta_g == 0:
        st.write("Reaction is at equilibrium.")
    else:
        st.write("Reaction is non-spontaneous.")

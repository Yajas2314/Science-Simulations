def run():
    import streamlit as st
    from components.formulas import display_formulas

    st.header("Atomic Structure")
    st.markdown("""
    Atoms consist of a nucleus containing protons and neutrons, surrounded by electrons in shells.
    
    **Key Concepts:**
    - Atomic number = Number of protons
    - Mass number = Protons + Neutrons
    - Electrons occupy shells (energy levels)
    """)

    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Atomic_Orbital_Probability_Density_1s.png/300px-Atomic_Orbital_Probability_Density_1s.png",
             caption="Electron Probability Cloud")

    formulas = [
        r"Z = \text{Atomic Number}",
        r"A = \text{Mass Number} = Z + N",
        r"E_n = -13.6 \frac{Z^2}{n^2} \text{ eV (Energy Levels)}"
    ]
    for f in formulas:
        st.latex(f)

    st.markdown("---")
    st.markdown("### Simple Electron Shell Visualization")

    # Simple interactive shell electron display
    total_electrons = st.slider("Select Number of Electrons (Atomic Number Z)", 1, 30, 10)
    
    shells = [2, 8, 18, 32]  # max electrons in shells 1,2,3,4 (simplified)
    distribution = []
    remaining = total_electrons
    for shell_capacity in shells:
        if remaining > shell_capacity:
            distribution.append(shell_capacity)
            remaining -= shell_capacity
        else:
            distribution.append(remaining)
            remaining = 0

    st.write("Electron distribution in shells:")
    for i, count in enumerate(distribution):
        if count > 0:
            st.write(f"Shell {i+1}: {count} electron(s)")

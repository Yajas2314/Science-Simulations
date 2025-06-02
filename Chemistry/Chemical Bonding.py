def run():
    import streamlit as st
    from components.formulas import display_formulas

    st.header("Chemical Bonding")
    st.markdown("""
    Atoms form bonds to achieve stable electron configurations.
    
    **Types of Bonding:**
    - Ionic Bonding: Transfer of electrons (e.g., NaCl)
    - Covalent Bonding: Sharing of electrons (e.g., H2O)
    - Metallic Bonding: Electron sea model
    
    """)

    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Covalent_bonding_in_HCl.svg/300px-Covalent_bonding_in_HCl.svg.png",
             caption="Covalent Bonding Example: HCl")

    formulas = [
        r"\text{Ionic Bonding: } \text{Na} + \text{Cl} \to \text{Na}^+ + \text{Cl}^-",
        r"\text{Covalent Bonding: } \text{H} + \text{H} \to \text{H}_2"
    ]
    for f in formulas:
        st.latex(f)

    st.markdown("---")
    st.markdown("### Interactive Ionic Bond Formation")

    ion1 = st.selectbox("Select Metal Ion", ["Na", "K", "Ca", "Mg"])
    ion2 = st.selectbox("Select Non-metal Ion", ["Cl", "F", "O", "S"])

    st.write(f"Formed Compound: {ion1}{ion2}")

    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Sodium-chloride-3D-ionic.png/300px-Sodium-chloride-3D-ionic.png",
             caption=f"{ion1}{ion2} Crystal Structure")

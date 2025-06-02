# main.py

import streamlit as st
import importlib

# Mapping of menu options to module paths
topics = {
    "Home": None,
    "Physics Lab 🧪": {
        "Reflection of Light": "physics.reflection",
        "Refraction of Light": "physics.refraction",
        "Dispersion of Light": "physics.dispersion",
        "Wave Optics": "physics.wave_optics",
        "Projectile Motion": "physics.projectile_motion",
        "Electrostatics": "physics.electrostatics",
        "Ohm's Law": "physics.ohms_law"
    },
    "Chemistry Lab ⚗️": {
        "Atomic Structure": "chemistry.atomic_structure",
        "Chemical Bonding": "chemistry.chemical_bonding",
        "Kinetics ": "chemistry.reaction_kinetics",
        "Thermodynamics": "chemistry.thermodynamics"
    }
}

st.set_page_config(page_title="Virtual Lab Simulator", layout="centered")

st.title("🔬 Virtual Physics & Chemistry Lab Simulator")

# Sidebar layout
lab_choice = st.sidebar.selectbox("Select Lab", ["Home", "Physics Lab 🧪", "Chemistry Lab ⚗️"])

if lab_choice == "Home":
    st.subheader("Welcome to the Virtual Lab!")
    st.markdown(
        """
        This simulator covers both Physics and Chemistry topics for students from Classes 9–12.
        
        - Visualize and interact with experiments.
        - See formulas and concepts applied in real time.
        - Use it as a powerful revision and learning tool.
        
        Select a lab from the sidebar to begin.
        """
    )

else:
    topic = st.sidebar.selectbox("Select Topic", list(topics[lab_choice].keys()))

    if topic:
        module_path = topics[lab_choice][topic]
        try:
            module = importlib.import_module(module_path)
            if hasattr(module, "run"):
                module.run()
            else:
                st.error("This topic doesn't have a 'run()' function.")
        except Exception as e:
            st.error(f"Failed to load module `{module_path}`.\n\nError: {str(e)}")

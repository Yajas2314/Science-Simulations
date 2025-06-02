# main.py

import streamlit as st
import importlib

# Mapping of menu options to module paths
topics = {
    "Home": None,
    "Physics Lab 🧪": {
        "Reflection of Light": "reflection.run",
        "Refraction of Light": "refraction.run",
        "Dispersion of Light": "dispersion.run",
        "Wave Optics": "wave_optics.run",
        "Projectile Motion": "projectile_motion.run",
        "Electrostatics": "electrostatics.run",
        "Ohm's Law": "ohms_law.run"
    },
    "Chemistry Lab ⚗️": {
        "Atomic Structure": "atomic_structure.run",
        "Chemical Bonding": "chemical_bonding.run",
        "Kinetics ": "reaction_kinetics.run",
        "Thermodynamics": "thermodynamics.run"
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

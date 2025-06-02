import streamlit as st

# Import all physics modules
from physics import (
    reflection, refraction, dispersion, wave_optics,
    projectile_motion, electrostatics, ohms_law
)

# Import all chemistry modules 
from chemistry import (
    atomic_structure, chemical_bonding, thermodynamics,
    reaction_kinetics
)

def main():
    st.set_page_config(page_title="Virtual Physics & Chemistry Lab", layout="wide")

    st.title("🧪 Virtual Physics & Chemistry Lab Simulator")

    st.sidebar.title("Select Subject")
    subject = st.sidebar.radio("Choose your lab:", ["Physics", "Chemistry"])

    if subject == "Physics":
        physics_topics = {
            "Reflection": reflection.run,
            "Refraction": refraction.run,
            "Dispersion": dispersion.run,
            "Wave Optics": wave_optics.run,
            "Projectile Motion": projectile_motion.run,
            "Electrostatics": electrostatics.run,
            "Ohm's Law": ohms_law.run
        }
        topic = st.sidebar.selectbox("Select Physics Topic:", list(physics_topics.keys()))
        st.sidebar.markdown("---")
        st.sidebar.write("Physics Concepts, Formulas, Simulations, Q&A")

        physics_topics[topic]()  # run the selected module

    else:  # Chemistry
        chemistry_topics = {
            "Atomic structure": atomic_structure.run,
            "Chemical bonding": chemical_bonding.run,
            "Thermodynamics": thermodynamics.run,
            "Reaction Kinetics": reaction_kinetics.run
        }
        topic = st.sidebar.selectbox("Select Chemistry Topic:", list(chemistry_topics.keys()))
        st.sidebar.markdown("---")
        st.sidebar.write("Chemistry Concepts, Reactions, Formulae, Q&A")

        chemistry_topics[topic]()  # run the selected module

if __name__ == "__main__":
    main()

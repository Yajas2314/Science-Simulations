# main.py
import streamlit as st
import importlib

st.set_page_config(page_title="Virtual Lab Simulator", layout="wide")
st.title("🧪🔬 Virtual Lab Simulator - Physics Only")

topics = [
    "Home",
    "Reflection of Light",
    "Refraction of Light",
    "Dispersion of Light",
    "Wave Optics",
    "Electrostatics",
    "Ohm's Law",
    "Projectile Motion"
]

choice = st.sidebar.selectbox("🔍 Select a Physics Topic", topics)

module_map = {
    "Reflection of Light": "reflection",
    "Refraction of Light": "refraction",
    "Dispersion of Light": "dispersion",
    "Wave Optics": "wave_optics",
    "Electrostatics": "electrostatics",
    "Ohm's Law": "ohms_law",
    "Projectile Motion" : "projectile_motion"
}

if choice == "Home":
    st.markdown("""
    ## 👋 Welcome to the Physics Virtual Lab
    This simulator allows you to:
    - Visualize **Physics** experiments
    - Understand concepts with **interactive plots**
    - Revise with **formulas** and **diagrams**

    Select a physics topic from the sidebar to begin.
    """)
else:
    module_name = module_map.get(choice)
    if module_name:
        try:
            module = importlib.import_module(module_name)
            if hasattr(module, "run"):
                module.run()
            else:
                st.warning(f"The module '{module_name}' does not have a 'run()' function.")
        except ModuleNotFoundError:
            st.error(f"Module '{module_name}' not found. Make sure '{module_name}.py' is in the same folder as main.py.")
        except Exception as e:
            st.error(f"Error loading simulation for {choice}: {e}")
    else:
        st.warning("Selected topic not available.")

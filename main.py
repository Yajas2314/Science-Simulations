# main.py

import os, sys
print("Current directory:", os.getcwd())
print("System path:", sys.path)

import streamlit as st
import importlib

st.set_page_config(page_title="Virtual Physics & Chemistry Lab Simulator", layout="wide")

st.markdown("<h1 style='text-align: center;'>🧪 Virtual Physics & Chemistry Lab Simulator</h1>", unsafe_allow_html=True)

lab_choice = st.selectbox("Select Lab", ["Physics Lab", "Chemistry Lab"])

# Define topic-to-module mappings
physics_topics = {
    "Reflection of Light": "physics.reflection",
    "Refraction of Light": "physics.refraction",
    "Dispersion of Light": "physics.dispersion",
    "Wave Optics": "physics.wave_optics",
    "Electrostatics": "physics.electrostatics",
    "Projectile Motion": "physics.projectile",
    "Ohm's Law": "physics.ohms_law"
}

chemistry_topics = {
    "Types of Chemical Reactions": "chemistry.chemical_reactions",
    "NCERT Reactions (9th–12th)": "chemistry.ncert_reactions",
    "Color Changes in Reactions": "chemistry.color_changes",
    "Organic Chemistry Reactions": "chemistry.organic_reactions"
}

# Get the appropriate topic list
if lab_choice == "Physics Lab":
    topic_dict = physics_topics
elif lab_choice == "Chemistry Lab":
    topic_dict = chemistry_topics
else:
    topic_dict = {}

# Display topic selection
selected_topic = st.selectbox("Select Topic", list(topic_dict.keys()))

# Load and run the selected module
if selected_topic:
    module_path = topic_dict[selected_topic]
    try:
        module = importlib.import_module(module_path)
        module.run()
    except Exception as e:
        st.error(f"Failed to load module `{module_path}.run`.\n\nError: {e}")

   

    

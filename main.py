import streamlit as st
from components.layout import show_header
from components.formulas import display_formulas
from components.questions import display_questions

from physics import (
    reflection, refraction, dispersion, wave_optics,
    electrostatics, ohms_law, projectile_motion
)

from chemistry import inorganic, organic, lab_simulations

st.set_page_config(page_title="Virtual Physics & Chemistry Lab", layout="wide")

show_header("🔬 Virtual Physics & Chemistry Lab Simulator")

lab_type = st.sidebar.selectbox("Select Lab", ["Physics", "Chemistry"])

if lab_type == "Physics":
    topic = st.sidebar.selectbox("Select Physics Topic", [
        "Reflection", "Refraction", "Dispersion",
        "Wave Optics", "Electrostatics",
        "Ohm's Law", "Projectile Motion"
    ])

    if topic == "Reflection":
        reflection.run()
        display_formulas("Reflection")
        display_questions("Reflection")
    elif topic == "Refraction":
        refraction.run()
        display_formulas("Refraction")
        display_questions("Refraction")
    elif topic == "Dispersion":
        dispersion.run()
        display_formulas("Dispersion")
        display_questions("Dispersion")
    elif topic == "Wave Optics":
        wave_optics.run()
        display_formulas("Wave Optics")
        display_questions("Wave Optics")
    elif topic == "Electrostatics":
        electrostatics.run()
        display_formulas("Electrostatics")
        display_questions("Electrostatics")
    elif topic == "Ohm's Law":
        ohms_law.run()
        display_formulas("Ohm's Law")
        display_questions("Ohm's Law")
    elif topic == "Projectile Motion":
        projectile_motion.run()
        display_formulas("Projectile Motion")
        display_questions("Projectile Motion")

elif lab_type == "Chemistry":
    topic = st.sidebar.selectbox("Select Chemistry Topic", [
        "Inorganic Reactions (NCERT)",
        "Organic Chemistry",
        "Lab Simulations"
    ])

    if topic == "Inorganic Reactions (NCERT)":
        inorganic.run()
        display_formulas("Inorganic")
        display_questions("Inorganic")
    elif topic == "Organic Chemistry":
        organic.run()
        display_formulas("Organic")
        display_questions("Organic")
    elif topic == "Lab Simulations":
        lab_simulations.run()
        display_formulas("Chemistry Simulations")

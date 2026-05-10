import streamlit as st

st.set_page_config(page_title="Mechanical Unit Converter", page_icon="⚙️")

st.title("⚙️ Mechanical Unit Converter and Material Density Checker")

st.markdown("""
### Student Information
*Full Name:* M.SaadKhan  
*Roll Number:* 25-ME-71
""")

st.divider()

st.header("🔁 Mechanical Unit Converter")

conversion_type = st.selectbox(
    "Select conversion type",
    ["Length", "Mass", "Force", "Pressure", "Temperature"]
)

value = st.number_input("Enter value", value=1.0)

if conversion_type == "Length":
    unit = st.selectbox("Convert", ["meter to feet", "feet to meter", "mm to inch", "inch to mm"])
    result = {
        "meter to feet": value * 3.28084,
        "feet to meter": value / 3.28084,
        "mm to inch": value / 25.4,
        "inch to mm": value * 25.4
    }[unit]

elif conversion_type == "Mass":
    unit = st.selectbox("Convert", ["kg to lb", "lb to kg", "gram to kg"])
    result = {
        "kg to lb": value * 2.20462,
        "lb to kg": value / 2.20462,
        "gram to kg": value / 1000
    }[unit]

elif conversion_type == "Force":
    unit = st.selectbox("Convert", ["Newton to kgf", "kgf to Newton"])
    result = {
        "Newton to kgf": value / 9.81,
        "kgf to Newton": value * 9.81
    }[unit]

elif conversion_type == "Pressure":
    unit = st.selectbox("Convert", ["Pa to bar", "bar to Pa", "psi to Pa", "Pa to psi"])
    result = {
        "Pa to bar": value / 100000,
        "bar to Pa": value * 100000,
        "psi to Pa": value * 6894.76,
        "Pa to psi": value / 6894.76
    }[unit]

else:
    unit = st.selectbox("Convert", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
    result = {
        "Celsius to Fahrenheit": (value * 9/5) + 32,
        "Fahrenheit to Celsius": (value - 32) * 5/9
    }[unit]

st.success(f"Converted Value = {result:.4f}")

st.divider()

st.header("🧱 Material Density Checker")

densities = {
    "Aluminum": 2700,
    "Steel": 7850,
    "Copper": 8960,
    "Brass": 8500,
    "Cast Iron": 7200,
    "Titanium": 4500,
    "Plastic": 950,
    "Wood": 700
}

material = st.selectbox("Select material", list(densities.keys()))
density = densities[material]

st.info(f"Density of {material} = {density} kg/m³")

volume = st.number_input("Enter volume in m³", value=1.0)
mass = density * volume

st.success(f"Mass of {material} = {mass:.2f} kg")

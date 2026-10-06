import streamlit as st

st.title("⚡ Calculadora de HP Pokémon")

# Slider de nível do Pokémon
level = st.slider("Selecione o nível do tamonfleme", min_value=1, max_value=100, value=25)

# Cálculo simplificado de estatística de HP base
hp_estimado = int((2 * 35 * level) / 100) + level + 10

st.write(f"Um **tamonfleme** no nível **{level}** tem aproximadamente **{hp_estimado} HP**!")
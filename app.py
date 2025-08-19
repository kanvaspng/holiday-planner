import streamlit as st
from backend.data_api import get_weather
from backend.scraper import get_events

st.set_page_config(page_title="Holiday Planner", layout="wide")

# Sidebar menu
page = st.sidebar.radio("Navigation", ["Overview", "Weather", "Nightlife", "Map", "Events", "Costs"])

if page == "Overview":
    st.title("Holiday Planner")
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/07/Tenerife_Beach.jpg", use_container_width=True)
    st.write("Why Tenerife is the perfect adventurous tropical getaway...")

elif page == "Weather":
    st.title("Weather")
    weather = get_weather("Tenerife")
    st.write(f"☀️ Max Temp: {weather['max_temp']}°C")

elif page == "Events":
    st.title("Events")
    events = get_events()
    for e in events:
        st.write(f"- {e}")

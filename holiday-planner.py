import streamlit as st

st.title("🌍 Holiday Planner")
st.subheader("Plan your dream holiday in Playa de las Americas!")
st.write("Use this website as your planning tool to explore the best weather, restaurants, and nightlife the area has to offer.")



import json
import streamlit as st
import pandas as pd


# Load JSON data
with open("app_data.json", "r") as f:
    data = json.load(f)

import streamlit as st

page = st.sidebar.radio("Navigate", ["Homepage", "Flights", "Weather", "Accommodation", "Restaurants", "Nightlife"])

if page == "Weather":
    # Page header
    st.header("Weather")
    
    # Main image
    st.image("beach.jpg", caption="Beautiful beach", use_container_width=True)
    
    # Subheading
    st.header("🌤️ September Weather Forecast")
    
    # Weather data
    september_weather = {
        1: {"temp": 28, "uv": 10, "wind": 24, "clouds": 31}, 2: {"temp": 23, "uv": 9, "wind": 22, "clouds": 55},
        3: {"temp": 24, "uv": 3, "wind": 28, "clouds": 97}, 4: {"temp": 23, "uv": 10, "wind": 24, "clouds": 52},
        5: {"temp": 24, "uv": 10, "wind": 20, "clouds": 40}, 6: {"temp": 24, "uv": 9, "wind": 22, "clouds": 13},
        7: {"temp": 24, "uv": 9, "wind": 26, "clouds": 11}, 8: {"temp": 24, "uv": 9, "wind": 28, "clouds": 26},
        9: {"temp": 24, "uv": 9, "wind": 20, "clouds": 33}, 10: {"temp": 24, "uv": 9, "wind": 15, "clouds": 23},
        11: {"temp": 25, "uv": 9, "wind": 13, "clouds": 25}, 12: {"temp": 25, "uv": 9, "wind": 19, "clouds": 4},
        13: {"temp": 26, "uv": 9, "wind": 19, "clouds": 3}, 14: {"temp": 26, "uv": 9, "wind": 20, "clouds": 28},
        15: {"temp": 26, "uv": 9, "wind": 22, "clouds": 1}, 16: {"temp": 26, "uv": 8, "wind": 24, "clouds": 2},
        17: {"temp": 25, "uv": 8, "wind": 20, "clouds": 6}, 18: {"temp": 25, "uv": 8, "wind": 15, "clouds": 12},
        19: {"temp": 26, "uv": 8, "wind": 28, "clouds": 30}, 20: {"temp": 26, "uv": 8, "wind": 35, "clouds": 4},
        21: {"temp": 26, "uv": 8, "wind": 39, "clouds": 3}, 22: {"temp": 26, "uv": 8, "wind": 9, "clouds": 3},
        23: {"temp": 26, "uv": 8, "wind": 24, "clouds": 2}, 24: {"temp": 25, "uv": 8, "wind": 26, "clouds": 5},
        25: {"temp": 25, "uv": 8, "wind": 26, "clouds": 20}, 26: {"temp": 26, "uv": 7, "wind": 26, "clouds": 2},
        27: {"temp": 26, "uv": 7, "wind": 24, "clouds": 24}, 28: {"temp": 26, "uv": 7, "wind": 22, "clouds": 3},
        29: {"temp": 26, "uv": 7, "wind": 24, "clouds": 31}, 30: {"temp": 26, "uv": 7, "wind": 28, "clouds": 6},
    }


    # Week selector
    week = st.selectbox("Select a week:", ["Choose a week", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5"])

    if week != "Choose a week":
        week_num = int(week.split()[-1])
        start_day = (week_num - 1) * 7 + 1
        end_day = min(start_day + 6, 30)
        days = list(range(start_day, end_day + 1))
        
        for i in range(0, len(days), 3):
            cols = st.columns(3)
            for j, day in enumerate(days[i:i+3]):
                day_data = september_weather.get(day, {})
                with cols[j]:
                    st.markdown(f"""
                    <div style="
                        background-color:#f0f2f6; 
                        padding:20px; 
                        border-radius:12px; 
                        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
                        text-align:center;
                    ">
                        <h4>September {day}</h4>
                        <p>🌡️ Temp: {day_data.get("temp","N/A")}°C</p>
                        <p>☀️ UV Index: {day_data.get("uv","N/A")}</p>
                        <p>💨 Wind: {day_data.get("wind","N/A")} km/h</p>
                        <p>☁️ Clouds: {day_data.get("clouds","N/A")}%</p>
                    </div>
                    """, unsafe_allow_html=True)

elif page == "Flights":
    import streamlit as st

    st.title("✈️ Flights to Tenerife")
    st.write("Find average prices and flight times from major UK airports to Tenerife South.")

    # Flight info dictionary
    flights_info = {
        "London Heathrow → Tenerife South": {"url": "https://www.skyscanner.net/transport/flights/lhr/tfs/", "avg_price": 215, "avg_time": "4h 25m"},
        "London Gatwick → Tenerife South": {"url": "https://www.skyscanner.net/transport/flights/lgw/tfs/", "avg_price": 220, "avg_time": "4h 30m"},
        "London Stansted → Tenerife South": {"url": "https://www.skyscanner.net/transport/flights/stn/tfs/", "avg_price": 210, "avg_time": "4h 35m"},
        "London Luton → Tenerife South": {"url": "https://www.skyscanner.net/transport/flights/ltn/tfs/", "avg_price": 205, "avg_time": "4h 40m"},
        "Manchester → Tenerife South": {"url": "https://www.skyscanner.net/transport/flights/man/tfs/", "avg_price": 200, "avg_time": "4h 35m"},
        "Birmingham → Tenerife South": {"url": "https://www.skyscanner.net/transport/flights/bhx/tfs/", "avg_price": 205, "avg_time": "4h 30m"},
        "Glasgow → Tenerife South": {"url": "https://www.skyscanner.net/transport/flights/glas/tfs/", "avg_price": 225, "avg_time": "4h 50m"}
    }

    # Display flights in 2-column layout
    flights_list = list(flights_info.items())
    for i in range(0, len(flights_list), 2):
        cols = st.columns(2)
        for j, (route, info) in enumerate(flights_list[i:i+2]):
            with cols[j]:
                st.markdown(f"### [{route}]({info['url']})")
                st.markdown(f"- **Average Price (September):** £{info['avg_price']}")
                st.markdown(f"- **Average Flight Time:** {info['avg_time']}")
                st.markdown("---")

elif page == "Accommodation":
    import streamlit as st
    import pandas as pd
    import folium
    from streamlit_folium import st_folium

    st.title("🏨 Accommodation")
    st.write("Browse hotels and Airbnbs with prices, ratings, and locations.")

    accommodations = data.get("accommodations", [])

    # Ensure accommodations is a list
    if isinstance(accommodations, dict):
        accommodations = [accommodations]

    if not accommodations:
        st.info("No accommodation data available.")
    else:
        df_acc = pd.DataFrame(accommodations)

        # Keep only relevant columns
        desired_cols = ["source", "title", "address", "lon", "lat", "nightly_price", "rating", "url"]
        df_acc = df_acc[[col for col in desired_cols if col in df_acc.columns]]

        # Format nightly_price with £
        if "nightly_price" in df_acc.columns:
            df_acc["nightly_price"] = df_acc["nightly_price"].apply(lambda x: f"£{x}" if pd.notnull(x) else x)

        # Normalize source for filtering
        if "source" in df_acc.columns:
            df_acc["source"] = df_acc["source"].str.lower()

        # Separate hotels and Airbnbs
        df_hotels = df_acc[df_acc["source"].str.contains("hotel", na=False)]
        df_airbnbs = df_acc[df_acc["source"].str.contains("airbnb", na=False)]

        # Remove unknown titles
        df_hotels = df_hotels[df_hotels["title"].str.lower() != "unknown"]
        df_airbnbs = df_airbnbs[df_airbnbs["title"].str.lower() != "unknown"]

        # Drop rows with missing nightly_price or rating for hotels
        df_hotels = df_hotels.dropna(subset=["nightly_price", "rating"])

        # --- Hotels Table ---
        st.subheader("Hotels")
        df_hotels_display = df_hotels.drop(columns=["source", "address", "lon", "lat"], errors="ignore")
        if not df_hotels_display.empty:
            st.dataframe(df_hotels_display, use_container_width=True)
        else:
            st.info("No hotel data available.")

        # --- Airbnb Table ---
        st.subheader("Airbnbs")
        df_airbnbs_display = df_airbnbs.drop(columns=["source", "lon", "lat"], errors="ignore")
        if not df_airbnbs_display.empty:
            st.dataframe(df_airbnbs_display, use_container_width=True)
        else:
            st.info("No Airbnb data available.")

        # --- Airbnb Map ---
        if not df_airbnbs.empty and all(col in df_airbnbs.columns for col in ["lat", "lon"]):
            # Center map on mean coordinates
            m = folium.Map(location=[df_airbnbs["lat"].mean(), df_airbnbs["lon"].mean()], zoom_start=12)

            # Add markers
            for _, row in df_airbnbs.iterrows():
                popup_html = f"""
                <b>{row['title']}</b><br>
                Price: {row['nightly_price']}<br>
                Rating: {row.get('rating', 'N/A')}<br>
                <a href="{row.get('url', '#')}" target="_blank">Link</a>
                """
                folium.Marker(
                    location=[row["lat"], row["lon"]],
                    popup=popup_html,
                    icon=folium.Icon(color="blue", icon="home", prefix="fa")
                ).add_to(m)

            st_folium(m, width=700, height=500)
        else:
            st.info("No Airbnb location data available.")


elif page == "Restaurants":
    st.header("Restaurants")
    st.image("restaurant.jpg", caption="Delicious food", use_container_width=True)

    restaurants = data.get("food_and_drink", [])
    if isinstance(restaurants, dict):
        restaurants = [restaurants]

    if restaurants:
        df_restaurants = pd.DataFrame(restaurants)
        if "distance_km" in df_restaurants.columns:
            df_restaurants = df_restaurants.sort_values("distance_km")
        
        st.dataframe(df_restaurants[['title', 'rating']], width=1000, height=400)

        # Map
        import folium
        from folium import DivIcon
        from streamlit_folium import st_folium
        from branca.element import Template, MacroElement

        df_food = df_restaurants.copy()
        df_food['type'] = df_food['category'].apply(lambda x: 'R' if x == 'restaurant' else 'B')
        map_center = [df_food['lat'].mean(), df_food['lon'].mean()]
        m = folium.Map(location=map_center, zoom_start=14)
        type_colors = {'R': 'red', 'B': 'blue'}

        for _, row in df_food.iterrows():
            color = type_colors[row['type']]
            folium.Marker(
                location=[row['lat'], row['lon']],
                popup=f"<b>{row['title']}</b><br>Rating: {row['rating']}",
                icon=DivIcon(html=f"""
                    <div style="
                        font-size:14px; color:white; 
                        background:{color}; 
                        border-radius:50%; 
                        width:25px; height:25px; 
                        display:flex; align-items:center; justify-content:center;
                        border: 2px solid white;">
                        {row['type']}
                    </div>
                """)
            ).add_to(m)

        # Legend
        template = """
        {% macro html(this, kwargs) %}
        <div style="
            position: fixed; 
            bottom: 50px; left: 50px; width:130px; 
            background-color: white; z-index:9999; 
            border:2px solid grey; border-radius:5px;
            padding: 10px;
            font-size:14px;">
        <b>Legend</b><br>
        <span style="
            color:white; background:red; 
            padding:3px 7px; border-radius:50%; display:inline-block; text-align:center;">R</span> Restaurant<br>
        <span style="
            color:white; background:blue; 
            padding:3px 7px; border-radius:50%; display:inline-block; text-align:center;">B</span> Bar
        </div>
        {% endmacro %}
        """
        macro = MacroElement()
        macro._template = Template(template)
        m.get_root().add_child(macro)

        st_folium(m, width=700, height=500)

    else:
        st.info("No restaurant data available.")

elif page == "Nightlife":
    import pandas as pd
    import folium
    from streamlit_folium import st_folium
    import streamlit as st

    # Page title
    st.title("Nightlife in Playa de las Americas")

    # Header and image
    st.header("Explore the vibrant nightlife!")
    st.image("bars.jpg", caption="Fun nightlife in Playa de las Americas", use_container_width=True)
    st.write("From lively bars to energetic clubs, discover the top spots in town.")

    # Nightlife data
    nightlife_data = [
        {"name": "Magic Lounge Club", "rating": 4.9, "address": "Av. Las Américas, S/N Mare Nostrum Resort, Cleopatra Palace, 38660 Playa de las Americas, Arona, Tenerife Spain", "latitude": 28.05496897023071, "longitude": -16.731087737540104},
        {"name": "Music Hall Tavern", "rating": 4.7, "address": "Carr General S/N Situated at Karting Las Americas just off Salida 78, 38660 Playa de las Americas, Arona, Tenerife Spain", "latitude": 28.064976864544448, "longitude": -16.73019483429926},
        {"name": "Tramps The King Of Clubs", "rating": 4.6, "address": "Avenida del Arquitecto Gomez Cuesta s/n C.C. Starco, 38650 Playa de las Americas, Arona, Tenerife Spain", "latitude": 28.0654060392919, "longitude": -16.73035495339176},
        {"name": "Sax Rock Bar", "rating": 4.4, "address": "Calle Mexico, 38650 Playa de las Americas, Arona, Tenerife Spain", "latitude": 28.061359920738358, "longitude": -16.733691107841604},
        {"name": "Kaluna Beach Club", "rating": 4.1, "address": "CC Centro Costa Local, 79, 38670 Playa de las Americas, Arona, Tenerife Spain", "latitude": 28.081174220841227, "longitude": -16.73591709329469},
        {"name": "Princess Di's", "rating": 4.4, "address": "Calle Mexico, 38660 Playa de las Americas, Arona, Tenerife Spain", "latitude": 28.06063179033841, "longitude": -16.733224106766844},
        {"name": "The Anchor Bar", "rating": 4.2, "address": None, "latitude": 28.0623916516338, "longitude": -16.729166277954462},
        {"name": "Diamond Social Club Tenerife", "rating": 5.0, "address": "Avenida Antonio Dominguez, 53 Residencial El Camisón, Local 50, 38650 Playa de las Americas, Arona, Tenerife Spain", "latitude": 28.05699118586703, "longitude": -16.72472384911588},
        {"name": "Lava Lounge Bar & Ristorante", "rating": 4.0, "address": "Av. Rafael Puig Lluvina, 4 Playa De Las Americas, local Numero 5, 38660 Playa de las Americas, Arona, Tenerife Spain", "latitude": 28.06552881119865, "longitude": -16.73094063199997},
        {"name": "Paradise Pool Bar", "rating": 4.5, "address": "Parque Santiago 2 Avenida de Rafael Puig Lluvina, 38660 Playa de las Americas, Arona, Tenerife Spain", "latitude": 28.060346887855356, "longitude": -16.733451731974764},
        {"name": "Hollands Heineken Cafe Tenerife", "rating": 4.6, "address": "Calle México, 38660 Playa de las Americas, Arona, Tenerife Spain", "latitude": 28.06119305100426, "longitude": -16.73377542219838},
        {"name": "Chill-out Bar", "rating": 4.2, "address": "Avda Rafel Puig 3 Playaflor Chill-Out Resort, 38660 Playa de las Americas, Arona, Tenerife Spain", "latitude": 28.0613242332813, "longitude": -16.73356369731705},
        {"name": "Leonardo's", "rating": 3.7, "address": "Avenida de Rafael Puig Lluvinia 9, 38660 Playa de las Americas, Arona, Tenerife Spain", "latitude": 28.063695186245308, "longitude": -16.73042522026066},
        {"name": "The Billy Tenerife", "rating": 4.6, "address": "Paseo Guadalajara, 38650 Playa de las Americas, Arona, Tenerife Spain", "latitude": 28.060386826253055, "longitude": -16.73302669333707},
        {"name": "Little Britain Tenerife Music Bar", "rating": 5.0, "address": "Avenida De Colón, Local 218 Puerto Colón, Santa Cruz De Tenerife, 38660 Playa de las Americas, Arona, Tenerife Spain", "latitude": 28.078687886857328, "longitude": -16.735938293310344},
        {"name": "Rags Bightclub Tenerife", "rating": 5.0, "address": "Avenida Arquitecto Gómez Cuesta 2 Veronicas Strip, Playa De Las Americas, 38660 Playa de las Americas, Arona, Tenerife Spain", "latitude": 28.065388016831868, "longitude": -16.73056582212672}
    ]

    # Convert to DataFrame and display top info
    df_nightlife = pd.DataFrame(nightlife_data)
    st.subheader("Top Nightlife Spots")
    st.dataframe(df_nightlife[['name', 'rating', 'address']])

    # Create Folium map
    m = folium.Map(location=[df_nightlife['latitude'].mean(), df_nightlife['longitude'].mean()], zoom_start=14)

    for _, row in df_nightlife.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"{row['name']} (Rating: {row['rating']})\nAddress: {row['address'] or 'N/A'}",
            tooltip=row['name']
        ).add_to(m)

    st.subheader("Map of Nightlife Locations")
    st_folium(m, width=700, height=500)

elif page == "Homepage":
    st.set_page_config(page_title="Travel Guide", page_icon="🏖️", layout="wide")

    st.title("🏖️ Welcome to Your Travel Guide")
    st.markdown("""
    Explore flights, weather, accommodation, restaurants, and nightlife to plan your perfect trip!
    """)

    # --- Navigation Cards ---
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("✈️ Flights"):
            st.session_state["page"] = "Flights"

    with col2:
        if st.button("☀️ Weather"):
            st.session_state["page"] = "Weather"

    with col3:
        if st.button("🏨 Accommodation"):
            st.session_state["page"] = "Accommodation"

    with col4:
        if st.button("🍽️ Restaurants"):
            st.session_state["page"] = "Restaurants"

    with col5:
        if st.button("🎉 Nightlife"):
            st.session_state["page"] = "Nightlife"

    # Optional: Quick Tips Section
    st.markdown("---")
    st.subheader("Quick Tips")
    st.markdown("""
    - Check ratings and reviews before booking or visiting places.  
    - Compare prices for flights and hotels to find the best deals.  
    - Explore maps and plan your routes efficiently.  
    """)

    import streamlit as st
    import requests

    st.set_page_config(page_title="Free LLM Chat", page_icon="🤖")
    st.title("🤖 Free LLM Chat")

    # Hugging Face API
    API_URL = "https://api-inference.huggingface.co/models/gpt2"  # small free model
    API_KEY = "YOUR_HUGGINGFACE_API_KEY"  # replace with your token
    headers = {"Authorization": f"Bearer {API_KEY}"}

    # Store chat history
    if "history" not in st.session_state:
        st.session_state.history = []

    # User input
    user_input = st.text_input("You:", key="input")

    if user_input:
        st.session_state.history.append(f"You: {user_input}")
        
        # Send request to Hugging Face
        response = requests.post(API_URL, headers=headers, json={"inputs": user_input})
        try:
            bot_reply = response.json()[0]["generated_text"]
        except:
            bot_reply = "Sorry, I couldn't process that."
        
        st.session_state.history.append(f"Bot: {bot_reply}")

    # Display chat history
    for msg in st.session_state.history:
        st.write(msg)





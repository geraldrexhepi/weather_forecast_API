import streamlit as st
import plotly.express as px  # import the module of plotly
from backend import get_data

# Add title, text input, slider, selectbox and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")    # we are capturing the place values to be used further down in the script
days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="Slide the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:  # when the user does not provide a place this will return an empty string
    # Get the data temp/sky
    filtered_data = get_data(place, days)

    # Create a temperature plot
    if option == "Temperature":
        dates = [dict["dt_txt"] for dict in filtered_data]
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    # Create sky conditions behaviour
    if option == "Sky":
        images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png", "Rain":"images/rain.png",
                  "Snow":"images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width=100)
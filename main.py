import streamlit as st
import plotly.express as px  # import the module of plotly

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")    # we are capturing the place values to be used further down in the script
days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="Sldie the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")



def get_data(days):
    dates = ["2023-11-11", "2023-11-12", "2023-11-13"]  # date format must be like year-month-day
    temperatures = [10, 14, 20]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x":"Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
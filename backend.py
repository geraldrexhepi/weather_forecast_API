import requests

apikey = "661bfbac8e53def92136ba3e4f341334"
def get_data(place, forecast_days=None, weather_type=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={apikey}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if weather_type == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if weather_type == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, weather_type="Temperature"))
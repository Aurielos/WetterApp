import requests

city = input("Bitte geben Sie einen Städtenamen ein")

api_key ="Your APIKey from OpenWeatherMap"

weather_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)

wetterbedingungen = {
    "clear sky": "klarer Himmel",
    "few clouds": "ein paar Wolken",
    "scattered clouds": "verstreute Wolken",
    "broken clouds": "bewölkt",
    "shower rain": "Regenschauer",
    "rain": "Regen",
    "thunderstorm": "Gewitter",
    "snow": "Schnee",
    "mist": "Nebel"
}

weather_data = requests.get(weather_url).json()

print("Stadt: ", weather_data["name"])
print("Wetter: ", wetterbedingungen.get(weather_data["weather"][0]["description"],
                                        weather_data["weather"][0]["description"]))
print("Temperatur: ", weather_data["main"]["temp"] - 273.15, "°C")
print("Luftfeuchtigkeit: ", weather_data["main"]["humidity"], "%")
print("Luftdruck: ", weather_data["main"]["pressure"], "hPa")

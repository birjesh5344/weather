import requests
import tkinter as tk
from tkinter import messagebox


def get_weather_data(location, unit='metric'):
    api_key = 'your_actual_api_key_here'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': location, 'appid': api_key, 'units': unit}

    response = requests.get(base_url, params=params)
    return response.json()


def display_weather_data():
    location = location_entry.get()
    unit = 'metric' if unit_var.get() == 'Celsius' else 'imperial'
    weather_data = get_weather_data(location, unit)

    if weather_data['cod'] == 200:
        city_label.config(text=f"City: {weather_data['name']}, {weather_data['sys']['country']}")
        temp_label.config(text=f"Temperature: {weather_data['main']['temp']}°{'C' if unit == 'metric' else 'F'}")
        humidity_label.config(text=f"Humidity: {weather_data['main']['humidity']}%")
        conditions_label.config(text=f"Conditions: {weather_data['weather'][0]['description']}")
    else:
        messagebox.showerror("Error", "Could not retrieve weather data. Please check the location and try again.")


# Initialize the GUI application
app = tk.Tk()
app.title("Weather App")

# Location input
tk.Label(app, text="Enter a city name or ZIP code:").pack()
location_entry = tk.Entry(app)
location_entry.pack()

# Unit selection
unit_var = tk.StringVar(value='Celsius')
tk.Radiobutton(app, text="Celsius", variable=unit_var, value='Celsius').pack()
tk.Radiobutton(app, text="Fahrenheit", variable=unit_var, value='Fahrenheit').pack()

# Fetch weather button
tk.Button(app, text="Get Weather", command=display_weather_data).pack()

# Weather data display
city_label = tk.Label(app, text="City: ")
city_label.pack()
temp_label = tk.Label(app, text="Temperature: ")
temp_label.pack()
humidity_label = tk.La

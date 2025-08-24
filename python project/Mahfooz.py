import requests
import tkinter as tk
from tkinter import messagebox

# Replace with your API key
API_KEY = "YOUR_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Function to fetch weather
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name!")
        return
    
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        result_label.config(
            text=f"📍 {city_name}, {country}\n"
                 f"🌡️ Temp: {temp}°C\n"
                 f"☁️ Condition: {weather}\n"
                 f"💧 Humidity: {humidity}%\n"
                 f"🌬️ Wind: {wind} m/s"
        )
    else:
        messagebox.showerror("Error", "City not found!")

# GUI Setup
root = tk.Tk()
root.title("Weather App 🌦️")
root.geometry("300x300")
root.resizable(False, False)

title_label = tk.Label(root, text="Weather App", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=5)

get_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
get_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()

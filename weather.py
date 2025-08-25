import tkinter as tk
from tkinter import messagebox, ttk
import requests
from datetime import datetime

class WeatherApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🌤️ Weather App")
        self.root.geometry("500x600")
        self.root.configure(bg='#87CEEB')
        
        # You need to get your own API key from openweathermap.org
        self.api_key = "fa65688c3a4233864cf42bde3a88435e"  # Replace with your actual API key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        
        self.setup_gui()
    
    def setup_gui(self):
        """Setup the GUI components"""
        
        # Main title
        title_label = tk.Label(
            self.root, 
            text="🌤️ Weather App", 
            font=('Arial', 24, 'bold'),
            bg='#87CEEB',
            fg='#003366'
        )
        title_label.pack(pady=20)
        
        # Input frame
        input_frame = tk.Frame(self.root, bg='#87CEEB')
        input_frame.pack(pady=10)
        
        tk.Label(
            input_frame, 
            text="Enter City Name:", 
            font=('Arial', 14),
            bg='#87CEEB',
            fg='#003366'
        ).pack(pady=5)
        
        self.city_entry = tk.Entry(
            input_frame, 
            font=('Arial', 14),
            width=20,
            justify='center'
        )
        self.city_entry.pack(pady=5)
        
        # Search button
        search_btn = tk.Button(
            input_frame,
            text="🔍 Get Weather",
            font=('Arial', 12, 'bold'),
            bg='#4CAF50',
            fg='white',
            command=self.get_weather,
            cursor='hand2',
            padx=20
        )
        search_btn.pack(pady=10)
        
        # Weather display frame
        self.weather_frame = tk.Frame(self.root, bg='#87CEEB')
        self.weather_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Info label
        info_label = tk.Label(
            self.root,
            text="💡 Get your free API key from openweathermap.org",
            font=('Arial', 10),
            bg='#87CEEB',
            fg='#666666'
        )
        info_label.pack(side='bottom', pady=10)
    
    def get_weather(self):
        """Fetch weather data from API"""
        city = self.city_entry.get().strip()
        
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name!")
            return
        
        if self.api_key == "YOUR_API_KEY_HERE":
            messagebox.showwarning(
                "API Key Required", 
                "Please get your API key from openweathermap.org and replace 'YOUR_API_KEY_HERE' in the code!"
            )
            return
        
        try:
            # API request
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'  # For Celsius
            }
            
            response = requests.get(self.base_url, params=params)
            
            if response.status_code == 200:
                data = response.json()
                self.display_weather(data)
            elif response.status_code == 404:
                messagebox.showerror("City Not Found", f"City '{city}' not found!")
            else:
                messagebox.showerror("Error", "Failed to fetch weather data!")
                
        except requests.exceptions.RequestException:
            messagebox.showerror("Network Error", "Please check your internet connection!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def display_weather(self, data):
        """Display weather information"""
        
        # Clear previous weather data
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
        
        # Extract data
        city_name = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        description = data['weather'][0]['description'].title()
        wind_speed = data['wind']['speed']
        
        # Get weather icon
        weather_icons = {
            'clear sky': '☀️',
            'few clouds': '🌤️',
            'scattered clouds': '⛅',
            'broken clouds': '☁️',
            'shower rain': '🌦️',
            'rain': '🌧️',
            'thunderstorm': '⛈️',
            'snow': '🌨️',
            'mist': '🌫️'
        }
        icon = weather_icons.get(description.lower(), '🌤️')
        
        # Create weather display
        weather_container = tk.Frame(self.weather_frame, bg='white', relief='raised', bd=2)
        weather_container.pack(fill='both', expand=True, padx=10, pady=10)
        
        # City name
        city_label = tk.Label(
            weather_container,
            text=f"📍 {city_name}, {country}",
            font=('Arial', 18, 'bold'),
            bg='white',
            fg='#003366'
        )
        city_label.pack(pady=10)
        
        # Weather icon and description
        weather_desc = tk.Label(
            weather_container,
            text=f"{icon} {description}",
            font=('Arial', 16),
            bg='white',
            fg='#333333'
        )
        weather_desc.pack(pady=5)
        
        # Temperature
        temp_label = tk.Label(
            weather_container,
            text=f"🌡️ Temperature: {temperature}°C",
            font=('Arial', 14, 'bold'),
            bg='white',
            fg='#FF6B35'
        )
        temp_label.pack(pady=5)
        
        # Feels like
        feels_label = tk.Label(
            weather_container,
            text=f"🤔 Feels like: {feels_like}°C",
            font=('Arial', 12),
            bg='white',
            fg='#666666'
        )
        feels_label.pack(pady=2)
        
        # Additional info frame
        info_frame = tk.Frame(weather_container, bg='white')
        info_frame.pack(pady=10)
        
        # Humidity
        humidity_label = tk.Label(
            info_frame,
            text=f"💧 Humidity: {humidity}%",
            font=('Arial', 12),
            bg='white',
            fg='#4CAF50'
        )
        humidity_label.pack(pady=2)
        
        # Pressure
        pressure_label = tk.Label(
            info_frame,
            text=f"📊 Pressure: {pressure} hPa",
            font=('Arial', 12),
            bg='white',
            fg='#2196F3'
        )
        pressure_label.pack(pady=2)
        
        # Wind speed
        wind_label = tk.Label(
            info_frame,
            text=f"💨 Wind Speed: {wind_speed} m/s",
            font=('Arial', 12),
            bg='white',
            fg='#9C27B0'
        )
        wind_label.pack(pady=2)
        
        # Timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time_label = tk.Label(
            weather_container,
            text=f"🕒 Updated: {timestamp}",
            font=('Arial', 10),
            bg='white',
            fg='#888888'
        )
        time_label.pack(pady=10)
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

# Run the application
if __name__ == "__main__":
    app = WeatherApp()
    app.run()
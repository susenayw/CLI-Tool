# devpulse/utils/weather.py

import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from devpulse.config import GEOCODING_API_URL, WEATHER_API_URL, DEFAULT_TIMEOUT

console = Console()

def get_coordinates(city_name: str):
    """Resolves city name to latitude and longitude."""
    params = {"name": city_name, "count": 1, "language": "en", "format": "json"}
    response = requests.get(GEOCODING_API_URL, params=params, timeout=DEFAULT_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    
    if not data.get("results"):
        return None
    
    result = data["results"][0]
    return {
        "name": result["name"],
        "country": result.get("country", "N/A"),
        "latitude": result["latitude"],
        "longitude": result["longitude"]
    }

def fetch_weather_data(city_name: str):
    """Fetches weather and returns structured dict (data, err)."""
    try:
        location = get_coordinates(city_name)
        if not location:
            return None, f"City '{city_name}' not found."

        params = {
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "current": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m"],
            "timezone": "auto"
        }
        res = requests.get(WEATHER_API_URL, params=params, timeout=DEFAULT_TIMEOUT)
        res.raise_for_status()
        weather = res.json()["current"]
        
        return {
            "city": location["name"],
            "country": location["country"],
            "temp": f"{weather['temperature_2m']} °C",
            "humidity": f"{weather['relative_humidity_2m']} %",
            "wind": f"{weather['wind_speed_10m']} km/h"
        }, None

    except requests.RequestException as e:
        return None, f"Network error: {str(e)}"
    except Exception as e:
        return None, f"Error: {str(e)}"

def fetch_weather(city_name: str):
    """CLI terminal rendering wrapper."""
    data, err = fetch_weather_data(city_name)
    if err:
        console.print(f"[bold red]Error:[/] {err}")
        return

    table = Table(title=f"Weather Forecast: {data['city']}, {data['country']}", style="cyan")
    table.add_column("Metric", style="bold white")
    table.add_column("Value", style="green")

    table.add_row("Temperature", data['temp'])
    table.add_row("Humidity", data['humidity'])
    table.add_row("Wind Speed", data['wind'])

    console.print(Panel(table, expand=False, border_style="blue"))
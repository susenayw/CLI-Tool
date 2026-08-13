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

def fetch_weather(city_name: str):
    """Fetches current weather and displays it in a Rich table."""
    try:
        with console.status(f"[bold green]Fetching weather for {city_name}..."):
            location = get_coordinates(city_name)
            
            if not location:
                console.print(f"[bold red]Error:[/] City '{city_name}' not found.", style="red")
                return

            params = {
                "latitude": location["latitude"],
                "longitude": location["longitude"],
                "current": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m"],
                "timezone": "auto"
            }
            res = requests.get(WEATHER_API_URL, params=params, timeout=DEFAULT_TIMEOUT)
            res.raise_for_status()
            weather_data = res.json()["current"]

        # Render output table
        table = Table(title=f"Weather Forecast: {location['name']}, {location['country']}", style="cyan")
        table.add_column("Metric", style="bold white")
        table.add_column("Value", style="green")

        table.add_row("Temperature", f"{weather_data['temperature_2m']} °C")
        table.add_row("Humidity", f"{weather_data['relative_humidity_2m']} %")
        table.add_row("Wind Speed", f"{weather_data['wind_speed_10m']} km/h")

        console.print(Panel(table, expand=False, border_style="blue"))

    except requests.RequestException as e:
        console.print(f"[bold red]Network Error:[/] Could not retrieve weather data. ({e})")
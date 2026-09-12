import requests


class WeatherActions:
    """Handles live weather information."""

    GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
    WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

    WEATHER_DESCRIPTIONS = {
        0: "clear sky",
        1: "mainly clear",
        2: "partly cloudy",
        3: "overcast",
        45: "foggy",
        48: "foggy",
        51: "light drizzle",
        53: "moderate drizzle",
        55: "heavy drizzle",
        56: "light freezing drizzle",
        57: "heavy freezing drizzle",
        61: "light rain",
        63: "moderate rain",
        65: "heavy rain",
        66: "light freezing rain",
        67: "heavy freezing rain",
        71: "light snow",
        73: "moderate snow",
        75: "heavy snow",
        77: "snow grains",
        80: "light rain showers",
        81: "moderate rain showers",
        82: "heavy rain showers",
        85: "light snow showers",
        86: "heavy snow showers",
        95: "thunderstorm",
        96: "thunderstorm with light hail",
        99: "thunderstorm with heavy hail",
    }

    def get_weather(self, location: str) -> str:
        """Return current weather for a location."""

        location = location.strip()

        if not location:
            return "Please tell me a location."

        try:
            coordinates = self._get_coordinates(location)

            if coordinates is None:
                return f"I couldn't find the location {location}."

            latitude, longitude, city_name = coordinates

            response = requests.get(
                self.WEATHER_URL,
                params={
                    "latitude": latitude,
                    "longitude": longitude,
                    "current": (
                        "temperature_2m,"
                        "relative_humidity_2m,"
                        "weather_code"
                    ),
                },
                timeout=10,
            )

            response.raise_for_status()

            data = response.json()
            current = data["current"]

            temperature = current["temperature_2m"]
            humidity = current["relative_humidity_2m"]
            weather_code = current["weather_code"]

            description = self.WEATHER_DESCRIPTIONS.get(
                weather_code,
                "unknown weather conditions",
            )

            return (
                f"The current weather in {city_name} is "
                f"{temperature} degrees Celsius, "
                f"{description}, with "
                f"{humidity}% humidity."
            )

        except requests.RequestException:
            return (
                "I couldn't retrieve the weather right now. "
                "Please check your internet connection and try again."
            )

        except (KeyError, TypeError, ValueError):
            return (
                "I received an unexpected weather response. "
                "Please try again later."
            )

    def _get_coordinates(self, location: str):
        """Return latitude, longitude, and city name."""

        response = requests.get(
            self.GEOCODING_URL,
            params={
                "name": location,
                "count": 1,
                "language": "en",
                "format": "json",
            },
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()
        results = data.get("results", [])

        if not results:
            return None

        result = results[0]

        return (
            result["latitude"],
            result["longitude"],
            result.get("name", location),
        )
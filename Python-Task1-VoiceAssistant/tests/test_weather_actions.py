from unittest.mock import patch, Mock

import requests

from src.actions.weather_actions import WeatherActions


def test_get_weather_returns_current_weather():
    weather = WeatherActions()

    mock_geocoding_response = Mock()
    mock_geocoding_response.json.return_value = {
        "results": [
            {
                "name": "Chennai",
                "latitude": 13.0827,
                "longitude": 80.2707,
            }
        ]
    }
    mock_geocoding_response.raise_for_status.return_value = None

    mock_weather_response = Mock()
    mock_weather_response.json.return_value = {
        "current": {
            "temperature_2m": 32.5,
            "relative_humidity_2m": 65,
            "weather_code": 1,
        }
    }
    mock_weather_response.raise_for_status.return_value = None

    with patch(
        "src.actions.weather_actions.requests.get",
        side_effect=[
            mock_geocoding_response,
            mock_weather_response,
        ],
    ) as mock_get:

        response = weather.get_weather("Chennai")

    assert mock_get.call_count == 2
    assert "Chennai" in response
    assert "32.5" in response
    assert "65%" in response
    assert "mainly clear" in response


def test_get_weather_returns_message_for_unknown_location():
    weather = WeatherActions()

    mock_response = Mock()
    mock_response.json.return_value = {
        "results": []
    }
    mock_response.raise_for_status.return_value = None

    with patch(
        "src.actions.weather_actions.requests.get",
        return_value=mock_response,
    ):
        response = weather.get_weather("UnknownPlace")

    assert response == (
        "I couldn't find the location UnknownPlace."
    )


def test_get_weather_handles_network_error():
    weather = WeatherActions()

    with patch(
        "src.actions.weather_actions.requests.get",
        side_effect=requests.RequestException(
            "Network error"
        ),
    ):
        response = weather.get_weather("Chennai")

    assert response == (
        "I couldn't retrieve the weather right now. "
        "Please check your internet connection and try again."
    )


def test_get_weather_handles_empty_location():
    weather = WeatherActions()

    response = weather.get_weather("")

    assert response == "Please tell me a location."
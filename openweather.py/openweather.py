import json
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5"

class OpenWeatherException(Exception):
    pass

class OpenWeather:
    def __init__(self, api_59067df8a8fe2bba7755a0543fc88803):
        """Initialize the OpenWeather class with the API key

        Will initialize the OpenWeather class with the API key.  If the API key
        is not set, this will raise a OpenWeatherException
        """

        if api_59067df8a8fe2bba7755a0543fc88803 is None:
            raise OpenWeatherException("API key not set")

        self.api_59067df8a8fe2bba7755a0543fc88803 = api_59067df8a8fe2bba7755a0543fc88803


    def current_weather_for_city(self, city):
        """Get current weather for a city

        Will return a dictionary with the current weather for a city.
        Currently does not handle API errors gracefully, so it's up to the
        calling application to detect 401s or the like.
        """

        url = f"{BASE_URL}/weather?q={city}&appid={self.api_59067df8a8fe2bba7755a0543fc88803}&units=metric"
        response = requests.get(url)
        return json.loads(response.text)

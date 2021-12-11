import json
from django.views.generic import View
from django.utils.translation import gettext as _
from django.shortcuts import render
from django.http import JsonResponse
import os
import requests
from django.core.cache import cache
import re
# forms
from .forms import WeatherForm


class WeatherForecastView(View):
    API_KEY = os.environ.get('WEATHER_API_KEY')
    WEATHER_API = "https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&lang={lang}"
    CACHE_TIME = 43200  # time in seconds for cache to be valid (6 Hours)
    
    def kelvin_to_celsius(self, kelvin):
        """
        Formula: T(°C) = T(K) - 273.15
        """
        return int(kelvin - 273.15)
    
    def kelvin_to_fahrenheit(self, kelvin):
        """
        Formula: T(°F) = 9/5(T(K) - 273.15) + 32
        """
        return int((kelvin - 273.15) * 1.8 + 32)
    
    def finalize_response(self, JSON_response):
        temp = JSON_response.get("main", {}).get("temp", 0)
        JSON_response["main"]["temp"] = self.kelvin_to_fahrenheit(temp)
        JSON_response["main"]["temp_celcius"] = self.kelvin_to_celsius(temp)
        JSON_response["main"]["temp_min"] = self.kelvin_to_celsius(JSON_response.get("main", {}).get("temp_min"))
        JSON_response["main"]["temp_max"] = self.kelvin_to_celsius(JSON_response.get("main", {}).get("temp_max"))
        JSON_response["main"]["feels_like"] = self.kelvin_to_celsius(temp)
        return JSON_response
    
    def post(self, request, *args, **kwargs):
        try:
            if self.request.method == "POST":
                city = request.POST.get("city")
                
                CACHE_KEY = "weather_" + re.sub('[^a-zA-Z]+', '', city)
                
                if cache.get(CACHE_KEY):
                    weather_data = cache.get(CACHE_KEY)
                    return JsonResponse(weather_data, status=200)
                else:
                    # return response object
                    API_ENDPOINT = self.WEATHER_API.format(CITY_NAME=city, API_KEY=self.API_KEY, lang=request.LANGUAGE_CODE)
                    response = requests.get(API_ENDPOINT)
                    responseJson = response.json()
                    
                    if responseJson.get("cod") == 200:
                        finalizedResponse = self.finalize_response(responseJson)
                        # set finalized reponse in cache
                        cache.set(CACHE_KEY, finalizedResponse, self.CACHE_TIME)
                        return JsonResponse(finalizedResponse, status=200)
                    else:
                        return JsonResponse(responseJson, status=400)
            return JsonResponse({"message": "Something went wrong!"}, status=400)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=400)


class HomePageView(View):
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, "pages/index.html", context=context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, "pages/index.html", context=context)

    def get_context_data(self, **kwargs):
        context = {}
        context["form"] = WeatherForm
        return context

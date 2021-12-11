from django.conf import settings
import json
from django.http import JsonResponse

# read city json data
city_json_data = open(f"{settings.STATIC_ROOT}data/cities.json")
desirializedCityData = json.load(city_json_data)
city_json_data.close()

def get_city_data(request):
    data = []
    cityData = []
    try:
        # get city name from request param (set initial value-A to shorten the initial response size)
        city_name = request.GET.get('term')
        
        if city_name:
            for city in desirializedCityData:
                if city['text'].lower().startswith(city_name.lower()):
                    cityData.append(city)
        else:
            cityData = desirializedCityData[0:500]
        data = {
            "results": cityData
        }
    except Exception as e:
        print(e)

    return JsonResponse(data=data, safe=False, status=200)

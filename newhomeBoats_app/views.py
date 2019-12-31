from django.shortcuts import render, HttpResponse, redirect
from .models import State, IBGECityCodes, City

# Create your views here.

def home(request):

    return render(request, 'home.html')

def load_allcities(request):
    data = {}

    qry_cities = City.objects.select_related("state").order_by("-state")
    res_cities = []
    res_all_cities = defaultdict(list)
    for city in qry_cities:
        res_cities.append(
            city.city + " - " + city.state.name + "_ " + city.state.country
        )
        res_all_cities[city.state.name].append(city.city)

    data["cityList"] = res_cities
    data["res_all_cities"] = dict(res_all_cities)

    return data
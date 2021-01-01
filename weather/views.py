import requests
from django.shortcuts import render


def index(request):

    appid = "3c77424120dc53262fe18cba74eb9d70"
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=' + appid
    city = 'London'
    res = requests.get(url.format(city))
    return render(request, 'weather/index.html')
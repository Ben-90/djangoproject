from django.shortcuts import render
import requests 
import json
# Create your views here.
def index(request):
    res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = res.json()
    houre = data['time']['updated']
    price = data['bpi']['EUR']['rate_float']
    prixfcfa = price* 655
    prixcom = price * 495
    return render(request, 'bitcoin/index.html', {
        'houre': houre,
        'price': price,
        'pricefc': prixfcfa,
        'pricecom': prixcom,
    })
from django.shortcuts import render
from django.http import HttpResponse

from pymongo import MongoClient
# Create your views here.


def home(request):
    return HttpResponse("Hello, world. You're at the goingout app index.")


def eating(request):
    places_to_eat = []
    conn = MongoClient('mongodb://127.0.0.1:27017')
    db = conn.going_out
    collection = db.places_to_eat
    for food in collection.find():
        print("Food is: ", food)
        places_to_eat.append(food)

    return HttpResponse(places_to_eat)

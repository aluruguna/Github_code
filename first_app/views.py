from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    favorite_book={'Raymond': "The Kite Runner",'Emma': "A Thousand Splendid Suns",'Denise': "The Great Gatsby"}
    return render(request, 'first_app/index.html', context=favorite_book)


def about(request):
    return HttpResponse("Hello from about")

def educative(request):
    return HttpResponse("Hello from Educative")


def age(request, age):
    return HttpResponse("Your age is {}".format(age))

def even_or_odd(request, num):
    if num % 2 == 0:
        output = "Num is even {}".format(num)
    else:
        output = "Num is odd {}".format(num)

    return HttpResponse(output)
    
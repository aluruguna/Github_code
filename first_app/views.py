from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchForm, TestForm, AnotherForm, PostModelForm

# Create your views here.

def index(request):
    favorite_book={'favorite_book':{'Raymond': "The Kite Runner",'Emma': "A Thousand Splendid Suns",'Denise': "The Great Gatsby"}}
    return render(request, 'first_app/index.html', context=favorite_book)


# def about(request):
#     about = {"value": "This is a random text"}
#     return render(request, 'first_app/about.html', context=about)

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

def home(request):
    return render(request,'first_app/home.html')

def search(request):
    return render(request,'first_app/search.html')

def about(request):
    return render(request,'first_app/about.html')

def forms(request):
    form = PostModelForm(request.POST or None)
    data = "None"
    text = "None"

    if form.is_valid():
        data = form.cleaned_data
        text= form.cleaned_data.get("text")
    return render(request, 'first_app/forms.html', {'form':form, 'data':data, 'text':text})

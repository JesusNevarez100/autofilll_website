from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.


def home(response):
    context = {}
    return render(response, 'main/home.html', context)




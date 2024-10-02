from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def displayQoute(request):
    return HttpResponse("The best investment we can makes is in ourself. - Warren Buffet")
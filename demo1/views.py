from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello, Django! from the main project repository and now has been updated")

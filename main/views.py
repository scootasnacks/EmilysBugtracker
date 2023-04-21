from django.shortcuts import render

# Create your views here.
# views.py file
from django.http import HttpResponse


def index(request):
    return HttpResponse("Test")
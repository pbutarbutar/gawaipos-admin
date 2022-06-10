from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings

# Create your views here.

def home(request):
    template = 'home.html'
    return render(request, template)
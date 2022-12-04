from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'qrticles/index.html')

def about(request):
    return render(request, 'qrticles/about.html')
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Beauty for your needs!")

def about(request):
    return HttpResponse("About us page!")

def services(request):
    return HttpResponse("Our Services page!")

def book(request):
    return HttpResponse("Book your appointment today!")
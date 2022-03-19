from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return  HttpResponse("<h2>hello</h2>")

def login(request):
    return render(request,'home.html')
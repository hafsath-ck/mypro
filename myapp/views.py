from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return  HttpResponse("<h2>hello</h2>")

def login(request):
    return render(request,'home.html')

def logout(request):
    return HttpResponse("<h2>bi</h2>")
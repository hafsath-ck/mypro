from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return  HttpResponse("<h2>hello</h2>")

def login(request):
    return render(request,'home.html')

def logout(request):
    return HttpResponse("<h2>bi</h2>")
     
def cssgrid(request):
    return render(request, 'cssgrid.html')

def bootstrapGrid(request):
    return render(request, 'bootsrap_grid.html')    

def javas(request):
    return render(request, 'javas.html')

def jsNew(request):
    return render(request, 'jsNew.html')  

def js_cond(request):
    return render(request, 'js_cond.html')  

def js_func(request):
    return render(request, 'js_func.html')

def dom_js(request):
    return render(request, 'dom_js.html')

def jsPractice(request):
    return render(request, 'jsPractice.html')

def jsPractice1(request):
    return render(request, 'jsPractice1.html')

def jsform_validation(req):
    return render(req, 'jsform_validation.html')

def calculator(request):
    return render(request, 'calculator.html')

def pattern(req):
    return render(req, 'pattern.html')

def jqeury(request):
    return render(request, 'jqeury.html')

def jqry_validation(request):
    return render(request, 'jqry_validation.html')
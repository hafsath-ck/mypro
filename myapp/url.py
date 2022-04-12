from unicodedata import name
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

    path('index', views.index, name = "index"),
    path('login', views.login, name = "login"),
    path('cssgrid', views.cssgrid, name = "cssgrid"),
    path('bootstrapGrid', views.bootstrapGrid, name="bootstrapGrid"),
    path('javas', views.javas, name = "javas"),
    path('jsNew' , views.jsNew, name = "jsNew"),
    path('js_cond', views.js_cond, name = "js_cond"),
    path('js_func', views.js_func, name = "js_funct"),
    path('dom_js', views.dom_js, name = "dom_js"),
    path('jsPractice', views.jsPractice, name = "jsPractice"),
    path('jsPractice1', views.jsPractice1, name = "jsPractice1"),
    path('jsform_validation', views.jsform_validation, name = "jsform_validation"),
    path('calculator', views.calculator, name = "calculator"),
    path('pattern', views.pattern, name = "pattern"),
    path('jqeury', views.jqeury, name = "jqeury"),
    path('jqry_validation', views.jqry_validation, name = "jqry_validation"),
]

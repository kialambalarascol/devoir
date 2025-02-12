from django.http import HttpResponse
from django.shortcuts import render

def accueil(request):
    return render(request, "accueil.html")

def information(request):
    return render(request,"info.html")
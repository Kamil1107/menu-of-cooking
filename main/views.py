from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'main/index.html')
def infa(request):
    return render(request, 'main/about.html')

def recipt(request,name):
    return render(request, f"main/{name}.html")

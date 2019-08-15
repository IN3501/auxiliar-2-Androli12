from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'miapp/index.html')

def equipodocente(request):
    return render(request, 'miapp/equipodocente.html')

def pestañalibre(request):
    return render(request, 'miapp/pestañalibre.html')

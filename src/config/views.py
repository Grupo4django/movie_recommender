from django.shortcuts import render

def home(request):
    """Vista principal del proyecto"""
    return render(request, 'home.html')

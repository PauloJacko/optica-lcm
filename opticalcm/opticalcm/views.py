from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def servicios(request):
    return render(request, 'servicios.html')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')

def convenios(request):
    return render(request, 'convenios.html')
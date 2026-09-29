from django.shortcuts import render


def inicio(request):
    return render(request, "juego/inicio.html")


def habitacion(request):
    return render(request, "juego/habitacion.html")
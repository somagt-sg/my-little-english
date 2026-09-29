from django.shortcuts import render


def inicio(request):
    return render(request, "juego/inicio.html")


def escenarios(request):
    return render(request, "juego/escenarios.html")


def habitacion(request):
    return render(request, "juego/habitacion.html")


def cocina(request):
    return render(request, "juego/cocina.html")
# users/views.py
from django.shortcuts import render
from .models import Usuario

def init_db(request):
    # Lógica para inicializar la base de datos con usuarios
    return render(request, 'init_db.html')

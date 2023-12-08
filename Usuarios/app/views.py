from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from .models import Usuario
from datetime import datetime
# Create your views here.


def index(request):
    context = {
        'username': 'Walter',
        'fecha_hoy' : datetime.now(),
        'anio' : '2023'
    }
    return render(request, 'app/index.html', context)

#VISTAS BASADAS EN CLASES

#LISTADO
class UsuarioListView(ListView):
    model = Usuario
    context_object_name = "usuario_listado"
    template_name = "app/usuario_listado.html" 
    extra_context= {'username': 'Walter',
        'fecha_hoy' : datetime.now(),
        'anio' : '2023'}

#CREAR
class UsuarioCreateView(CreateView):
    model = Usuario  
    template_name = "app/usuario_crear.html"  
    success_url= "listado"
    fields = "__all__"
    extra_context= {'username': 'Walter',
        'fecha_hoy' : datetime.now(),
        'anio' : '2023'}

#MOSTRAR USUARIO ESPECIFICO
class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = "app/usuario_detalle.html"
    extra_context= {'username': 'Walter',
        'fecha_hoy' : datetime.now(),
        'anio' : '2023'}

#MODIFICAR
class UsuarioUpdateView(UpdateView):
    model = Usuario  
    template_name = "app/usuario_modificar.html"  
    success_url = "listado"
    fields = "__all__" 
    extra_context= {'username': 'Walter',
        'fecha_hoy' : datetime.now(),
        'anio' : '2023'}

    def get_success_url(self):
        return reverse("usuario_detalle", kwargs={"pk":self.object.pk})

#BORRAR    
class UsuarioDeleteView(DeleteView):
    model = Usuario  
    template_name = "app/usuario_borrar.html"  
    success_url = reverse_lazy("usuario_listado")
    extra_context= {'username': 'Walter',
        'fecha_hoy' : datetime.now(),
        'anio' : '2023'}
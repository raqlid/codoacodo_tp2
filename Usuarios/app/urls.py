from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("listado",views.UsuarioListView.as_view(), name="usuario_listado"),
    path("crear", views.UsuarioCreateView.as_view(), name="usuario_crear"),
    path("detalle/<pk>", views.UsuarioDetailView.as_view(), name="usuario_detalle"),
    path("modificar/<pk>", views.UsuarioUpdateView.as_view(), name="usuario_modificar"),
    path("borrar/<pk>", views.UsuarioDeleteView.as_view(), name="usuario_borrar"),
]
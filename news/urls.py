from django.urls import path
from .views import home, articoloDetailView,listaArticoli, giornalistaDetailView

app_name = 'news'

urlpatterns = [
    #path('', home, name="homeview"),
    path("giornalista_detail/<int:pk>", giornalistaDetailView, name="giornalista_detail"),
    path("lista_articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("lista_articoli/", listaArticoli, name="listaArticoli"),
]
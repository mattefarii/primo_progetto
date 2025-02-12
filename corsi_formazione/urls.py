from django.urls import path
from .views import viewA, viewB, viewC, viewD, viewE

app_name = 'corsi_formazione'

urlpatterns = [
    #path('', home, name="homeview"),
    path("viewA/", viewA, name="viewA"),
    path("viewB/", viewB, name="viewB"),
    path("viewC/", viewC, name="viewC"),
    path("viewD/", viewD, name="viewD"),
    path("viewE/", viewE, name="viewE"),

]
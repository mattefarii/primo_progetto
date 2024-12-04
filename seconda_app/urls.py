from django.urls import path, include
from seconda_app.views import es_if, if_else_elif, index2, es_for




app_name = "seconda_app"
urlpatterns = [
    path('', index2, name = "index2"),
    path ('es_if', es_if, name='es_if'),
    path ("if_else_elif", if_else_elif, name = "if_else_elif"),
    path ("es_for", es_for, name = "es_for"),

    
]
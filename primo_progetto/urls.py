from django.contrib import admin
from django.urls import path,include

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include("prima_app.urls", namespace="prima_app")),
        
]

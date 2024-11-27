from django.contrib import admin
from django.urls import path,include
from primo_progetto.views import index_root

urlpatterns = [
        path('admin/', admin.site.urls),
        path('prima_app/', include("prima_app.urls", namespace="prima_app")),
        path('', index_root, name = "index_root"),
        
]

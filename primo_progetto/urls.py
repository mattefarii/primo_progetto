from django.contrib import admin
from django.urls import path,include
from primo_progetto.views import index_root

urlpatterns = [
        path('', index_root, name = "index_root"),
        path('admin/', admin.site.urls),
        path('prima_app/', include("prima_app.urls", namespace="prima_app")),
        path('seconda_app/', include("seconda_app.urls", namespace="seconda_app")),
        path('news/', include("news.urls", namespace="news")),
        path('corsi_formazione/', include("corsi_formazione.urls", namespace="corsi_formazione")),
        path('accounts/', include('django.contrib.auth.urls')),
]

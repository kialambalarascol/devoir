from django.urls import path

from appT.views import accueil

urlpatterns = [
    path('accueil/', accueil),
]


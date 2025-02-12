from django.urls import path
from appT.views  import accueil
from appT.views import information

app_name="appT"

urlpatterns = [
    path('',accueil),
    path('information/',information),
]


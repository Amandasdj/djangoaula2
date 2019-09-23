from django.urls import path #importa as urls para um caminho
from . import views

urlpatterns = [
    path('', views.index, name='Index')
]
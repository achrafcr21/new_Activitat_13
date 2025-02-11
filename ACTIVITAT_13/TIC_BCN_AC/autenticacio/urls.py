from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_sin_sesion, name='login'),
    path('login_con_sesion/', views.login_con_sesion, name='login_con_sesion'),
    path('inicio/', views.inicio, name='inicio'),
]

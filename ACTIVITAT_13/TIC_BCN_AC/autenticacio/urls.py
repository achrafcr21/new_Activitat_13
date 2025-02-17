from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_con_sesion, name='login'),
    path('login-sin-sesion/', views.login_sin_sesion, name='login_sin_sesion'),
    path('inicio/', views.inicio, name='inicio'),
    path('logout/', views.logout, name='logout'),
]

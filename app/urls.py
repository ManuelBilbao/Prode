from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.fixture, name='fixture'),
    path('', views.fixture, name='password_change_done'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('cambiar_pass/', auth_views.password_change, name='cambiar_contrasenia'),
    path('actualizar/<int:partido_pk>:<int:prediccion_pk>/', views.actualizar_prediccion, name='actualizar_prediccion'),
    path('nuevo/<int:partido_pk>/', views.crear_prediccion, name='crear_prediccion'),
    path('puntos/', views.puntos, name='puntos'),
    path('ver/<int:partido_pk>/', views.ver_predicciones, name='ver_predicciones'),
]

"""prode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.fixture, name='fixture'),
    path('', views.fixture, name='password_change_done'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('cambiar_pass/', auth_views.password_change, name='cambiar_contrasenia'),
    path('actualizar/<int:partido_pk>:<int:prediccion_pk>/', views.actualizar_prediccion, name='actualizar_prediccion'),
    path('nuevo/<int:partido_pk>/', views.crear_prediccion, name='crear_prediccion'),
    path('puntos/', views.puntos, name='puntos')
]

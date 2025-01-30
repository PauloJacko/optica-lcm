from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),  
    path('servicios/', views.servicios, name='servicios'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),
    path('convenios/', views.convenios, name='convenios'),
]


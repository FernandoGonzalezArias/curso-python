from django.urls import path
from . import views

urlpatterns =[
   path('add/', views.form),
   path('listado/', views.listado, name='listado')
]
from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new),
    path('new-address/',views.new_address),
    
]
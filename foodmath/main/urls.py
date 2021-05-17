from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_main),
    path('menu/', views.food_menu)
]
from django.urls import path
from food_app import views

urlpatterns = [
    path('', views.home, name='home'),
]

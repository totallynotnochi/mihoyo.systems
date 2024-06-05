from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpagereturn, name="MainPage"),
    path('generic.html/', views.optimizerreturn, name="Optimizer")
    ]
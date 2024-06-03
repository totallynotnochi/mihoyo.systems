from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpagereturn, name="Main Page"),
    path('dev/', views.htmldevreturn)
    ]
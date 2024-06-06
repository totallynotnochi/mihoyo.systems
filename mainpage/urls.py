from django.urls import path
from . import views

urlpatterns = [
    path('', views.genshin_uid_input, name="MainPage"),
    path('generic.html/', views.optimizerreturn, name="OptimizerAccess"),
    path('dev/', views.optimizerreturn, name="DevPage"),
    path('uid-loaded-index/', views.uid_loaded_index, name='uid_loaded_index')
    ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.genshin_uid_input, name="MainPage"),
    path('generic.html/', views.optimizerreturn, name="OptimizerAccess"),
    path('devx/', views.uid_loaded_index, name="DevPage"),
    path('uid-loaded-index/', views.uid_loaded_index, name='uid_loaded_index'),
    path('advancedStats/', views.advancedStats, name="advancedStats"),
]
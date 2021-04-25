from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('eating/', views.eating, name='eating')
]

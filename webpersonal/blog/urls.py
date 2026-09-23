from django.urls import path
from . import views

urlpatterns = [
    path('<int:slug>/', views.detial, name='detail'),
    path("", views.index, name="index")
]
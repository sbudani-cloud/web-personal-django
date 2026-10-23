from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('<slug:slug>/', views.detail, name='detail'),
    path("", views.index, name="index"),
    path("search_results", views.search_results, name="search-results"),
    path('<slug:slug>/like/', views.like_post, name='like_post'),
]
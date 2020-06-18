from django.contrib import admin
from django.urls import path
from planet import views

urlpatterns = [
    path('posts/', views.post_list, name='home'),
    path('posts/<str:category_name>/',views.post_list, name='post-list')
]

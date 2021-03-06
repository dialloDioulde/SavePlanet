from django.contrib import admin
from django.urls import path
from planet import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='view-post'),
    path('posts/<str:category_name>/',views.post_list, name='post-list'),
    path('posts/detail/<int:post_id>/',views.post_detail, name='post-detail'),
    path('posts/detail/<int:post_id>/<str:message>/',views.post_detail, name='post-detail-message'),


    path('createPost/', views.create_post, name='create-post'),
    path('editPost/<int:post_id>/', views.edit_post, name='edit-post'),
    path('deletePost/<int:post_id>/', views.delete_post, name='delete-post'),

    path('editComment/<int:comment_id>/', views.edit_comment, name='edit-comment'),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name='delete-comment'),


    path('createUser/', views.create_user, name='create-user'),
    path('loginUser/', views.login_user, name='login-user'),
    path('logoutUser/', views.logout_user, name='logout-user'),
    path('profilUser/', views.profil_user, name='profil-user'),
    path('editUser/', views.edit_user, name='edit-user'),
    path('password/', views.change_password, name='change-password'),
    path('deleteUser/', views.delete_user, name='delete-user'),

]

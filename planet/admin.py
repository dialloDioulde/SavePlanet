from django.contrib import admin
from django.db import models
from django.forms import Textarea
from planet.models import PostCategory, Post, Comment
# Register your models here.


# Afficher la table PostCategory dans l'admin
@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    pass


# Afficher la table Post dans l'admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Les champs de recherche
    search_fields = ['title', ]

    # Les colonnes de la table Post à afficher
    list_display = ('title', 'category', 'published', 'created_at', 'comments_count')

    # Critères de filtre
    list_filter = ('category__name', 'published',)

    # Autocomplétion sur le champ Category
    autocomplete_fields = ['category']

    # Surcharger les TextField dans django Admin
    formfield_overrides = {models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 100})}}

    # Pour récupérer le nombre de Commentaire d'un Post
    def comments_count(self, obj):
        return Comment.objects.filter(post = obj).count()
    comments_count.short_description = 'Comments' # Pour ajouter le résulat dans la colonne Comments

    pass


# Afficher la table Comment dans l'admin
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Les champs de recherche
    search_fields = ['post__title', 'author_name']

    # Les colonnes de la table Post à afficher
    list_display = ['post', 'user', 'text', 'status', 'moderation_text', 'created_at']

    # Les Champs qui seront éditables dans l'admin
    list_editable = [ 'status', 'moderation_text',]

    # Filtrer les Commentaires par Statut
    list_filter = ('status',)

    # Autocomplétion sur les champs title et author_name
    #autocomplete_fields = ['post']
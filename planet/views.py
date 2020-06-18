from django.shortcuts import render, get_object_or_404
from planet.models import *
from planet import model_helpers, navigation

# Create your views here.


def post_list(request, category_name = model_helpers.post_category_all.slug()):

    category, posts = model_helpers.get_category_and_posts(category_name)
    categories = model_helpers.get_categories()

    context = {'category' : category, 'posts' : posts, 'categories' : categories,
               'navigation_items' : navigation.navigation_items(navigation.NAV_POSTS)}

    return render(request, 'planet/post_list.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    context = {'post' : post, 'navigation_items' : navigation.navigation_items(navigation.NAV_POSTS)}
    return render(request, 'planet/post_detail.html', context)
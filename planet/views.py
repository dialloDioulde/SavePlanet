from django.shortcuts import render
from planet.models import *
from planet import model_helpers

# Create your views here.


def post_list(request, category_name = model_helpers.post_category_all.slug()):
    category, posts = model_helpers.get_category_and_posts(category_name)

    context = {'category' : category, 'posts' : posts}

    return render(request, 'planet/post_list.html', context)
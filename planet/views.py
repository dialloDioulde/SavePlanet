from django.shortcuts import render
from planet.models import *
# Create your views here.
def post_list(request):
    posts = Post.objects.all()

    context = {'posts' : posts}

    return render(request, 'planet/post_list.html', context)
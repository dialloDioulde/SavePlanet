from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.decorators.csrf import csrf_protect

from planet.models import *
from planet import model_helpers, navigation
from  planet.forms import CreateCommentForm, CreatePostForm, CreateUserForm, EditUserForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
# Create your views here.



# Home
def home(request):
    context = {'navigation_items' : navigation.navigation_items(navigation.NAV_HOME),}
    return render(request, 'planet/home.html', context)


# Renvoie tous les Posts et on affiche les plus récents
def post_list(request, category_name = model_helpers.post_category_all.slug()):

    category, posts = model_helpers.get_category_and_posts(category_name)
    categories = model_helpers.get_categories()

    context = {'category' : category, 'posts' : posts, 'categories' : categories,
               'navigation_items' : navigation.navigation_items(navigation.NAV_POSTS)}

    return render(request, 'planet/post_list.html', context)


# Renvoie les details d'un Post
def post_detail(request, post_id, message = ''):
    post = get_object_or_404(Post, pk=post_id) # On récupère le Post par son ID

    # On récupère que les Posts d'une même Catégorie ici
    posts_same_category = Post.objects.filter(published = True, category = post.category).exclude(pk = post_id)

    # On récupère les Commentaires liés au Post en question
    posts_comments = post.comments.exclude(status = Comment.STATUS_HIDDEN).order_by('created_at')

    # Création de Commentaire pour le Post en question
    comment_form = CreateCommentForm()
    comment_form = CreateCommentForm(request.POST or None)
    if request.method == 'POST' :
        if comment_form.is_valid():
            comment = comment_form.save(commit= False)
            comment.post = post
            comment.save()

            args = [post.pk, ' Votre Commentaire a bien été Publié ! ']
            return HttpResponseRedirect(reverse('post-detail-message', args = args) + '#comments')
        else:
            comment_form = CreateCommentForm()

    context = {'post' : post, 'navigation_items' : navigation.navigation_items(navigation.NAV_POSTS),
               'posts_same_category' : posts_same_category, 'comments' : posts_comments,
               'comment_form' : comment_form, 'message' : message }
    return render(request, 'planet/post_detail.html', context)



# Création de Post
def create_post(request):
    post_form = CreatePostForm(request.POST or None)
    if request.method == 'POST':
        if post_form.is_valid():
            post_form.save()
            return redirect('view-post')
            # args = [post.pk, ' Votre Commentaire a bien été Publié ! ']
            # return HttpResponseRedirect(reverse('post-detail-message', args=args) + '#comments')
        else:
            post_form = CreatePostForm()

    #context = {'post_form': post_form}
    context = { 'navigation_items' : navigation.navigation_items(navigation.NAV_CREATE_POST), 'post_form' : post_form }

    return render(request, 'planet/create_post.html', context)



# Inscription d'un Utilisateur
@csrf_protect
def create_user(request):
    user_form = CreateUserForm(request.POST)
    if request.method == 'POST':
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('view-post')
    else:
        user_form = CreateUserForm()

    context = {'navigation_items' : navigation.navigation_items(navigation.NAV_CREATE_USER), 'user_form' : user_form }

    return render(request, 'planet/user/create_user.html', context)


# Connexion de l'Utilisateur
def login_user(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request = request, data = request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.INFO, "Bienvenue")
                return redirect('view-post')
            else:
                messages.error(request, "Nom d'Utilisateur ou Mot de Passe Incorrecte")
        else:
            messages.error(request, "Nom d'Utilisateur ou Mot de Passe Incorrecte")

    login_form = AuthenticationForm()

    context = {'navigation_items': navigation.navigation_items(navigation.NAV_LOGIN_USER), 'login_form': login_form}

    return render(request, "planet/user/login_user.html", context)



# Déconnexion de l'Utilisateur
@login_required
def logout_user(request):
    logout(request)
    messages.info(request, "Déconnexion Réussie !")
    return redirect("view-post")


# Profil de l'Utilisateur
def profil_user(request):
    context = {'navigation_items': navigation.navigation_items(navigation.NAV_PROFIL_USER), 'user' : request.user}
    return render(request, "planet/user/profil_user.html", context)



# Édition des Informations de l'Utilisateur
@login_required
def edit_user(request):
    if request.method == "POST":
        edit_user_form = EditUserForm(request.POST, instance=request.user)

        if edit_user_form.is_valid():
            edit_user_form.save()
            return redirect("profil-user")
    else:
        edit_user_form = EditUserForm(instance=request.user)
        context = { 'navigation_items': navigation.navigation_items(navigation.NAV_EDIT_USER), 'edit_user_form': edit_user_form}
        return render(request, "planet/user/edit_user.html", context)



@login_required
def change_password(request):
    if request.method == "POST":
        change_password_form = PasswordChangeForm(data=request.POST, user=request.user)

        if change_password_form.is_valid():
            change_password_form.save()
            update_session_auth_hash(request, change_password_form.user)
            messages.success(request, f" Mot De Passe Modifier avec Succès !")
            return redirect("profil-user")
        else:
            messages.info(request, f" Les Mots de Passes que vous avez taper ne corresponent pas, veuillez recommencer !")
            return redirect("change-password")
    else:
        change_password_form = PasswordChangeForm(user=request.user)

        context = { 'navigation_items': navigation.navigation_items(navigation.NAV_CHANGE_PASSWORD), 'change_password_form': change_password_form}
        return render(request, "planet/user/change_password.html", context)



@login_required
def delete_user(request):
    user = User.objects.get(id= request.user.pk)
    user.delete()
    return redirect('view-post')

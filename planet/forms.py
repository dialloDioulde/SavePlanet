from planet.models import *
from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


# Création d'un Post
class CreatePostForm(forms.ModelForm):
    class Meta :
        model = Post
        fields = ['title', 'category', 'text' ]


# Édition d'un Post
class EditPostForm(forms.ModelForm):
    class Meta :
        model = Post
        fields = ['title', 'category', 'text' ]


# Création d'un Commentaire
class CreateCommentForm(forms.ModelForm):
    class Meta :
        model = Comment
        fields = ['text', ]


# Création d'un Commentaire
class EditCommentForm(forms.ModelForm):
    class Meta :
        model = Comment
        fields = ['text', ]



# Inscription d'un Utilisateur
class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def save(self, commit = True):
        user = super(CreateUserForm, self).save(commit = False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit :
            user.save()

        return user


# Édition des Informations de l'Utilisateur
# Edit Profile
class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

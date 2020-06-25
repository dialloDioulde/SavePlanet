from django.urls import reverse_lazy

# Dans ce document on definit les onglets de notre barre de navigation

NAV_HOME = 'HOME'
NAV_POSTS = 'POSTS'
NAV_PROFIL_USER = ''
NAV_EDIT_USER = ''
NAV_CHANGE_PASSWORD = ''
NAV_CREATE_POST = ''
NAV_EDIT_POST = ''
NAV_LOGIN_USER = ''
NAV_CREATE_USER = ''


NAV_ITEMS = ( (NAV_HOME, reverse_lazy('home')),
              (NAV_POSTS, reverse_lazy('view-post')),
              (NAV_CREATE_POST, reverse_lazy('create-post')),
              (NAV_EDIT_POST, reverse_lazy('edit-post')),

              (NAV_LOGIN_USER, reverse_lazy('login-user')),
              (NAV_CREATE_USER, reverse_lazy('create-user')),
              (NAV_PROFIL_USER, reverse_lazy('profil-user')),
              (NAV_EDIT_USER, reverse_lazy('edit-user')),
              (NAV_CHANGE_PASSWORD, reverse_lazy('change-password')),  )

def navigation_items(selected_item):
    items = []
    for name, url in NAV_ITEMS :
        items.append({
            'name': name,
            'url': url,
            'active': True if selected_item == name else False
        })

    return items

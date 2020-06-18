from planet.models import Post, PostCategory, Comment


post_category_all = PostCategory(name='all')

def get_category_and_posts(category_name):
    # On filtre les Posts par leur statut de publication
    posts = Post.objects.filter(published = True)

    # On récupère les Posts de toutes les Catégories
    if category_name == post_category_all.slug() :
        category = post_category_all
    else:
        try:
            # On récupère que les Posts dont le nom est égale à category_name
            category = PostCategory.objects.get(name__iexact = category_name) # On ne tient pas de la Casse
            posts = posts.filter(category = category)
        except PostCategory.DoesNotExist :
            # Si la catégorie de Posts n'existe pas
            category = PostCategory(name=category_name)
            posts = Post.objects.none()

    posts = posts.order_by('-created_at')
    return category, posts
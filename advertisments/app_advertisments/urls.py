from django.urls import path
from .views import index
from .views import top_sellers
from .views import register
from .views import advertisement_post
# from .views import advertisement
from .views import login
from .views import profile
from .views import advertisement_detail

#Ссылки на страницы
urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers.html', top_sellers, name='top-sellers'),
    path('register.html', register),
    path('advertisement-post.html', advertisement_post),
    # path('advertisement.html', advertisement),
    path('login.html', login),
    path('profile.html', profile),
    path('advertisement/<int:pk>', advertisement_detail, name='adv-detail')
]
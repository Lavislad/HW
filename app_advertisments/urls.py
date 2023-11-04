from django.urls import path
from .views import index
from .views import top_sellers
from .views import register
from .views import advertisement_post
from .views import advertisement

urlpatterns = [
    path('', index),
    path('top-sellers.html', top_sellers),
    path('register.html', register),
    path('advertisement-post.html', advertisement_post),
    path('advertisement.html', advertisement),
]
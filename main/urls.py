from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('posts', views.posts, name='posts'),
    path('achievements', views.achievements, name='achievements'),
    path('create-post', views.create_post, name='create_post'),
    path('create-achievement', views.create_post, name='create_achievement'),
]

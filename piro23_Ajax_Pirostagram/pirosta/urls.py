from django.urls import path
from . import views

app_name = 'pirosta'

urlpatterns = [
    path('', views.index, name='index'), 
    path('post/create/', views.post_create, name='post_create'), 
    path('post/<int:post_id>/like/', views.like_toggle, name='like_toggle'), 
    path('post/<int:post_id>/comment/create/', views.comment_create, name='comment_create'), 
    path('comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'), 
    path('search/', views.search_posts, name='search_posts'), 
]
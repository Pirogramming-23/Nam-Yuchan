from django.urls import path
from . import views

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('upload/', views.idea_upload, name='idea_upload'),
    path('<int:pk>/', views.idea_detail, name='idea_detail'),
    path('<int:pk>/update/', views.idea_update, name='idea_update'),
    path('<int:pk>/delete/', views.idea_delete, name='idea_delete'),
    
    #AJAX URL
    path('update_interest/', views.update_interest, name='update_interest'),
    path('star_idea/', views.star_idea, name='star_idea'),
]
from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.review_list, name='review_list'), # 리뷰 리스트 페이지
    path('<int:pk>/', views.review_detail, name='review_detail'), # 리뷰 디테일 페이지
    path('create/', views.review_create, name='review_create'), # 새 리뷰 작성 페이지
    path('<int:pk>/update/', views.review_update, name='review_update'), # 리뷰 수정 페이지
    path('<int:pk>/delete/', views.review_delete, name='review_delete'), # 리뷰 삭제
]
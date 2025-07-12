from django import forms
from .models import MovieReview

class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = [
            'title', 'release_year', 'genre', 'rating',
            'running_time_minutes', 'review_content', 'director', 'actors'
        ]
        widgets = {
            'review_content': forms.Textarea(attrs={'rows': 10, 'placeholder': '영화에 대한 리뷰를 작성해주세요.'}),
            'rating': forms.NumberInput(attrs={'step': 0.5, 'min': 0.0, 'max': 5.0, 'placeholder': '(0.5단위)'}),
            'title': forms.TextInput(attrs={'placeholder': '영화 제목'}),
            'release_year': forms.NumberInput(attrs={'placeholder': '예: 2023'}),
            'running_time_minutes': forms.NumberInput(attrs={'placeholder': '예: 120 (분 단위)'}),
            'director': forms.TextInput(attrs={'placeholder': '예: 봉준호'}),
            'actors': forms.TextInput(attrs={'placeholder': '예: 송강호, 최우식'}),
        }
        labels = {
            'title': '제목',
            'release_year': '개봉년도',
            'genre': '장르',
            'rating': '별점',
            'running_time_minutes': '러닝타임',
            'review_content': '리뷰',
            'director': '감독',
            'actors': '배우',
        }
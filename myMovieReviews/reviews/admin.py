from django.contrib import admin
from .models import MovieReview

@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'genre', 'rating', 'director', 'actors', 'created_at')
    list_filter = ('genre', 'release_year')
    search_fields = ('title', 'director', 'actors', 'review_content')
    ordering = ('-created_at',)
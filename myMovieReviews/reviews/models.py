from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class MovieReview(models.Model):
    title = models.CharField(max_length=100, verbose_name="영화 제목")
    release_year = models.IntegerField(verbose_name="개봉 년도")
    genre_choices = [
        ('SF', 'SF'),
        ('Comedy', '코미디'),
        ('Action', '액션'),
        ('Drama', '드라마'),
        ('Horror', '공포'),
        ('Thriller', '스릴러'),
        ('Fantasy', '판타지'),
        ('Animation', '애니메이션'),
        ('Romance', '로맨스'),
        ('Mystery', '미스터리'),
        ('Crime', '범죄'),
        ('Musical', '뮤지컬'),
    ]
    genre = models.CharField(max_length=50, choices=genre_choices)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    running_time_minutes = models.IntegerField()
    review_content = models.TextField()
    director = models.CharField(max_length=100, blank=True, null=True)
    actors = models.CharField(max_length=200,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
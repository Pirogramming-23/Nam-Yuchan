from django.db import models

class Post(models.Model):
    author_username = models.CharField(max_length=50)
    image = models.ImageField(upload_to='posts/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.author_username} - {self.content[:20]}'

    @property
    def total_likes(self):
        return self.likes_count

    @property
    def total_comments(self):
        return self.comments.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_username = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.post.author_username}] {self.author_username}: {self.text[:20]}'

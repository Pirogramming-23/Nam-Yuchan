from django.db import models
from devtools.models import DevTool

class Idea(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='idea_images/')#업로드 경로
    content = models.TextField()
    interest = models.IntegerField(default=0)
    devtool = models.ForeignKey(DevTool, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

class IdeaStar(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    starred_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.idea.title} star'
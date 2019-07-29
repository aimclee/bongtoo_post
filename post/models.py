from django.db import models

# Create your models here.

class Post(models.Model):
    image = models.FileField(upload_to="images/%Y/%m/%d/") 
    title = models.CharField(max_length = 100)
    body = models.TextField()

    def __str__(self):
        return self.title




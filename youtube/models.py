from django.db import models

class VideoModel(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='videos/')
    filename = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

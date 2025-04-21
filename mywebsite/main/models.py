from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=100)
    version = models.CharField(max_length=20, blank=True)
    exe_file = models.FileField(upload_to='games/')

    def __str__(self):
        return self.title
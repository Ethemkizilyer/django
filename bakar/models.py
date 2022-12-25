from django.db import models

# Create your models here.

class Bakar(models.Model):
    path_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.path_name}"
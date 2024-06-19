from django.db import models
from apps.categories.models import Category

class Movies(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    release = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"ID: {self.id} Title: {self.title}"

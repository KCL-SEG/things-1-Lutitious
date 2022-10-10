from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

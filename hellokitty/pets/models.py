from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Pet(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    adoption_date = models.DateField(auto_now_add=True)
    weight = models.IntegerField()
    height = models.IntegerField()
    details = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    deleted = models.BooleanField(null=True)

    class Meta:
        ordering = ['adoption_date']

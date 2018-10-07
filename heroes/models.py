from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=50)
    secret_identity = models.CharField(max_length=50)
    super_power = models.CharField(max_length=20)
    strength = models.IntegerField(default=1)
    inserted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Villain(Hero):
    pass
from django.db import models
from .choices import *


# Create your models here.
class Users(models.Model):
    city = models.CharField(max_length=150)
    auto_column = models.CharField(max_length=150)
    channel = models.TextField(choices=channel)
    epic = models.TextField(choices=epic)
    user = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.user}'

    def save(self, **kwargs):
        super().save()


class Cities(models.Model):
    city_choice = models.CharField(max_length=150)

    def save(self, **kwargs):
        super().save()


class AC(models.Model):
    ac_choice = models.CharField(max_length=150)

    def save(self, **kwargs):
        super().save()


class NewUser(models.Model):
    nu_choice = models.CharField(max_length=150)

    def save(self, **kwargs):
        super().save()

from django.db import models


class Donor(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=25)

from django.db import models


class Administration(models.Model):
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class Organization(models.Model):
    name = models.CharField(max_length=250)
    address = models.TextField()
    type = models.CharField(max_length=20)
    contact_no = models.IntegerField()

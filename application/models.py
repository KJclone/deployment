from django.db import models

class database(models.Model):
    Name=models.CharField(max_length=100)
    Number=models.CharField(max_length=100)

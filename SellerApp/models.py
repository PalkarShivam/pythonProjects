from django.db import models

class Laptop(models.Model):
    CompanyName=models.CharField(max_length=32)
    ModelName=models.CharField(max_length=32)
    RAM=models.IntegerField()
    ROM=models.IntegerField()
    Price=models.FloatField()

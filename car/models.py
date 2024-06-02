from django.db import models

class Registration(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=50)
    
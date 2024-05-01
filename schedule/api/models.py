from django.db import models

# Create your models here.
class UserDetails(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)

class Column(models.Model):
    name = models.CharField(max_length=200)

class Card(models.Model):
    title = models.CharField(max_length=200)
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    userid = models.ForeignKey(UserDetails, on_delete=models.CASCADE)


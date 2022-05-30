from atexit import register
from django.db import models

# Create your models here.
class UserData(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    captured_on = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.first_name+self.last_name

class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    register_on = models.DateTimeField(auto_now_add=True)


from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
import datetime
from django.template.defaultfilters import truncatechars

from django.utils.safestring import mark_safe
from traitlets import default

# Create your models here.

class Unknown(models.Model):
    id = models.BigAutoField(primary_key=True)
    captured_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'unknown/%y')
    @property
    def short_description(self):
        return truncatechars(self.description,20)
    
    def unknown_photo(self):
        return mark_safe('<img src="{}" width="100" height="50"/>'.format(self.image.url))
    unknown_photo.short_description = "Image"
    unknown_photo.allow_tags = True


class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'photos/%y')
    roll_no = models.IntegerField()
    captured_on = models.DateTimeField(auto_now_add=True)

    @property
    def short_description(self):
        return truncatechars(self.description,20)
    
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" height ="100" />'.format(self.image.url))
    admin_photo.short_description = "Image"
    admin_photo.allow_tags = True

    def __str__(self) -> str:
        return self.first_name+self.last_name

# class Person(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     register_on = models.DateTimeField(auto_now_add=True)

class PersonVisit(models.Model):
    id = models.BigAutoField(primary_key=True)
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    captured_onn = models.DateTimeField()
    
    def __str__(self) -> str:
        return str(self.id)
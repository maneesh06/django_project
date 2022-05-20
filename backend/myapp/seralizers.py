from dataclasses import fields
from rest_framework import serializers
from myapp.models import UserData

class UserDataSeralizer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['id','first_name','last_name']

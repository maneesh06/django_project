from dataclasses import fields
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from myapp.models import UserData

class UserDataSeralizer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['id','first_name','last_name','captured_on']

class SetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 2
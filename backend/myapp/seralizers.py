from dataclasses import fields
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from myapp.models import Person,PersonVisit

class PersonSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','first_name','last_name','captured_on','roll_no','admin_photo']
    


class PersonVisitSeralizer(serializers.ModelSerializer):
    class Meta:
        model = PersonVisit
        fields = ['id','person','captured_onn']

class SetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 2
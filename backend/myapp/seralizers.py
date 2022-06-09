from dataclasses import fields
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from myapp.models import Person,PersonVisit,Unknown

class PersonSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','first_name','last_name','captured_on','roll_no','admin_photo']

class PersonVisitSeralizer(serializers.ModelSerializer):
    class Meta:
        model = PersonVisit
        fields = ['id','person','captured_onn']

class UnknownVisitSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Unknown
        fields = ['id','captured_onn',"image"]
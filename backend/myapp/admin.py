from dataclasses import field
from django.contrib import admin
from .models import Person,PersonVisit

class PersonVisitInline(admin.TabularInline):
    model = PersonVisit
    list_display = ("person","captured_onn","id")
    fields = ("person","captured_onn","id")
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [PersonVisitInline]
    list_display= ("first_name","last_name","id")
    fields = ("first_name","last_name")

# Register your models here.

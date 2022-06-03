from dataclasses import field
from django.contrib import admin
from .models import Person,PersonVisit

class PersonVisitInline(admin.TabularInline):
    model = PersonVisit
    list_display = ("person","captured_onn","id")
    readonly_fields = ("person","captured_onn","id")
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [PersonVisitInline]
    list_display= ("first_name","last_name","id","captured_on")
    # fields = ("first_name","last_name")
    readonly_fields=("first_name","last_name","id","captured_on")

# Register your models here.

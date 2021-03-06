
from django.contrib import admin

from .models import Person,PersonVisit,Unknown
from django.views.decorators.csrf import csrf_exempt

class PersonVisitInline(admin.TabularInline):
    model = PersonVisit
    list_display = ("person","captured_onn","id")
    readonly_fields = ("person","captured_onn","id")
@csrf_exempt
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [PersonVisitInline]
    list_display= ("first_name","last_name","id","captured_on","roll_no",'admin_photo')
    # fields = ("first_name","last_name")
    readonly_fields=("id","captured_on")
@csrf_exempt
@admin.register(Unknown)
class Unknown(admin.ModelAdmin):
    list_display = ("id","captured_on","unknown_photo")
    readonly_fields = ("id","captured_on","unknown_photo")

# Register your models here.

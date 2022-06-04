from dataclasses import field
from django.utils.safestring import mark_safe
from django.contrib import admin
from matplotlib import image
from .models import Person,PersonVisit
from django.utils.safestring import mark_safe

class PersonVisitInline(admin.TabularInline):
    model = PersonVisit
    list_display = ("person","captured_onn","id")
    readonly_fields = ("person","captured_onn","id")
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [PersonVisitInline]
    list_display= ("first_name","last_name","id","captured_on","roll_no",'admin_photo')
    # fields = ("first_name","last_name")
    readonly_fields=("id","captured_on")

    # def _image(self, obj:Person):
    #     return mark_safe( f"<a href='{/django_project/backend/DSC_0052.JPG}'>{self.image}</a>" )
        # return "hello"

# Register your models here.

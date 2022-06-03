from django.forms import BaseModelFormSet,modelformset_factory
from .models import Person

class BaseAuthorFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = Person.objects.all()

AuthorFormSet = modelformset_factory(Person, fields=('first_name', 'last_name','id','captured_on'), formset=BaseAuthorFormSet)
author_form=AuthorFormSet(queryset=Person.objects.all())
print(author_form)
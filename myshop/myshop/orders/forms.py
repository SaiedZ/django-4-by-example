from typing import Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from django.utils import translation

from localflavor.us.forms import USZipCodeField
from localflavor.es.forms import ESPostalCodeField

from .models import Order


# class LocalizedZipCodeField(forms.Field):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields = {
#             'en': USZipCodeField(),
#             'es': ESPostalCodeField(),
#         }

#     def clean(self, value):
#         language = translation.get_language()
#         field = self.fields[language]
#         return field.clean(value)


class OrderCreateForm(forms.ModelForm):
    # postal_code = LocalizedZipCodeField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Détecter la langue actuelle
        language = translation.get_language()

        # Choisir le champ de code postal en fonction de la langue
        if language.startswith('en'):
            self.fields['postal_code'] = USZipCodeField()
        elif language.startswith('es'):
            self.fields['postal_code'] = ESPostalCodeField()
        else:
            self.fields['postal_code'] = forms.CharField()

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']

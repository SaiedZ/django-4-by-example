from django import forms
from .models import Image


class ImageCreateForm(forms.ModelForm):

    class Meta:

        model = Image
        fields = ['title', 'url', 'description']
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        valid_extensions = ['jpg', 'jpeg']

        url = self.cleaned_data['url']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError(
                'The given URL does not match valid image extensions.'
            )
        return url

import requests
import httpx

from django.core.files.base import ContentFile
from django.utils.text import slugify
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
        extension = self._get_extension(url)
        if extension not in valid_extensions:
            raise forms.ValidationError(
                'The given URL does not match valid image extensions.'
            )
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = self._get_extension(image_url)
        image_name = f'{name}.{extension}'

        with httpx.Client() as client:
            response = client.get(image_url)
            if response.status_code == 200:
                image.image.save(image_name, ContentFile(
                    response.content), save=False)
            else:
                raise forms.ValidationError(
                    f"The given URL, {image_url}, does not match valid "
                    f"image extensions. Status code: {response.status_code}"
                )

        if commit:
            image.save()
        return image

    # def save(self, force_insert=False, force_update=False, commit=True):
    #     image = super().save(commit=False)
    #     image_url = self.cleaned_data['url']
    #     name = slugify(image.title)
    #     extension = self._get_extension(image_url)
    #     image_name = f'{name}.{extension}'
    #     # download image from the given URL
    #     response = requests.get(image_url)
    #     image.image.save(image_name, ContentFile(response.content), save=False)
    #     if commit:
    #         image.save()
    #     return image

    def _get_extension(self, url):
        return url.rsplit('.', 1)[1].lower()

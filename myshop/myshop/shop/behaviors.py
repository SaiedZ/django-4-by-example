
from django.conf import settings


class WithDefaultImageUrl:

    def get_image_url(self) -> str:
        if image := getattr(self, 'image', None):
            return image.url

        return settings.DEFAULT_IMAGE_URL

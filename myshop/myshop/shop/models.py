from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields

from .behaviors import WithDefaultImageUrl


class Category(TranslatableModel):

    translations = TranslatedFields(
        name=models.CharField(max_length=200),
        slug=models.SlugField(max_length=200, unique=True)
    )

    class Meta:
        # https://django-parler.readthedocs.io/en/latest/compatibility.html#the-ordering-meta-field
        # ordering = ['name']
        # indexes = [
        #     models.Index(fields=['name']),
        # ]

        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(WithDefaultImageUrl, TranslatableModel):

    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    translations = TranslatedFields(
        name=models.CharField(max_length=200),
        slug=models.SlugField(max_length=200)
    )
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # https://django-parler.readthedocs.io/en/latest/compatibility.html#the-ordering-meta-field
        # ordering = ['name']
        indexes = [
            # models.Index(fields=['id', 'slug']),
            # models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse('shop:product_detail', args=[self.id, self.slug])

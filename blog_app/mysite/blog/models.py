from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    class Meta:
        # by default the default manager is objects or the first defined
        default_manager_name = "objects"

        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"], name="publish_desc_index"),
        ]

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f"Post(title={self.title}, author={self.author}), id={self.id})"

    def get_absolute_url(self) -> str:
        return reverse(
            "blog:post_detail",
            args=[self.id],
        )

from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated

    # def location(self, obj):
    # """
    # Used to implement the location method
    # to return the canonical URL for each object
    # in the sitemap.
    # default get_absolute_url() method is used
    # to return the URL of each object.
    # """
    #     return obj.get_absolute_url()

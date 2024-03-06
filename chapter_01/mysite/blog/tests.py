import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post


@pytest.mark.django_db
def test_post_list_view(client):
    url = reverse('blog:post_list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_detail_view(client):
    user = User.objects.create_user(username='user', password='testpass')
    post = Post.objects.create(
        author=user,
        title='Test Post',
        slug='test-post',
        body='Test Content',
        status=Post.Status.PUBLISHED,
    )
    url = reverse('blog:post_detail', args=[post.id])
    response = client.get(url)
    assert response.status_code == 200
    assert 'Test Post' in response.content.decode()

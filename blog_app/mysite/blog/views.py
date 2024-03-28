from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import (
    Paginator, EmptyPage, PageNotAnInteger
)
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.postgres.search import TrigramSimilarity
from django.views.decorators.http import require_POST
from django.core.mail import send_mail

from taggit.models import Tag

from .models import Post, Comment
from .forms import EmailPostForm, CommentForm, SearchForm
from django.core.mail import send_mail


# def post_list(request):

#     post_list = Post.published.all()
#     paginator = Paginator(post_list, 1)
#     page_number = request.GET.get('page', 1)

#     try:
#         posts = paginator.page(page_number)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)

#     return render(request, "blog/post/list.html", {"posts": posts})


class PostListView(ListView):
    """
    A class-based view to display a list of published posts.
    """
    model = Post
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 1
    template_name = 'blog/post/list.html'

    def dispatch(self, request, *args, **kwargs):
        tag_slug = self.kwargs.get('tag_slug')
        if tag_slug is not None:
            self.tag = get_object_or_404(Tag, slug=tag_slug)
        else:
            self.tag = None
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.tag:
            queryset = queryset.filter(tags__in=[self.tag])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context


def post_detail(request, year: int, month: int, day: int, post: str):

    post_obj = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )

    comments = post_obj.comments.filter(active=True)
    form = CommentForm()

    post_tags_ids = post_obj.tags.values_list('id', flat=True)
    similar_posts = (
        Post.published
            .filter(tags__in=post_tags_ids)
            .exclude(id=post_obj.id)
            .annotate(same_tags=Count('tags'))
            .order_by('-same_tags', '-publish')[:4]
    )

    return render(
        request,
        'blog/post/detail.html',
        {
            'post': post_obj,
            'comments': comments,
            'form': form,
            'similar_posts': similar_posts,
        }
    )


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id,
                             status=Post.Status.PUBLISHED)
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = (
                f"{cd['name']} recommends you read "
                f"{post.title}"
            )
            message = (
                f"Read {post.title} at {post_url}\n\n"
                f"{cd['name']}\'s comments: {cd['comments']}"
            )
            send_mail(subject, message, 'your_account@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(
        request, 'blog/post/share.html',
        {'post': post,
         'form': form,
         'sent': sent}
    )


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(
        Post, id=post_id,
        status=Post.Status.PUBLISHED
    )
    comment = None
    form = CommentForm(data=request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

    return render(
        request, 'blog/post/comment.html',
        {'post': post,
         'form': form,
         'comment': comment}
    )


def post_search(request):

    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']

            # search_vector = SearchVector('title', 'body', config='english')
            # give more relevance to posts that are matched by title
            # rather than by content
            # search_vector = (
            #     SearchVector('title', weight='A')
            #     + SearchVector('body', weight='B')
            # )
            # search_query = SearchQuery(query, config='english')
            # results = (
            #     Post.published
            #     .annotate(
            #         search=search_vector,
            #         rank=SearchRank(search_vector, search_query)
            #     )
            #     .filter(search=search_query)
            #     .filter(rank__gte=0.3)
            #     .order_by('-rank')
            # )

            # allow for misspellings
            # example search ` yango ` will return `django` results
            # A trigram is a group of three consecutive characters.
            results = Post.published.annotate(
                similarity=TrigramSimilarity('title', query)
            ).filter(similarity__gt=0.1).order_by('-similarity')

    return render(
        request, 'blog/post/search.html',
        {'form': form,
         'query': query,
         'results': results}
    )

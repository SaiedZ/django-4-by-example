import logging

from django.http import JsonResponse, HttpRequest, HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django import forms as django_forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import ImageCreateForm

from .models import Image


logger = logging.getLogger(__name__)


@login_required
def image_create(request):

    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            try:
                new_item = form.save(commit=False)
            except django_forms.ValidationError:
                messages.error(
                    "The URL you provided is invalid. Please provide a valid URL."
                )
                return redirect('images:create')

            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)

    return render(
        request,
        'images/image/create.html',
        {
            'section': 'images',
            'form': form
        }
    )


@login_required
def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(
        request,
        'images/image/detail.html',
        {
            'section': 'images',
            'image': image
        }
    )


@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')

    if image_id and action:
        try:
            image = Image.prefetch_related('users_like').get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Image.DoesNotExist:
            logging.error(
                f"Image with id {image_id} not found. "
                f"request sent by user {request.user}"
            )
    return JsonResponse({'status': 'error'})


@login_required
def image_list(request: HttpRequest):

    images = Image.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    images_only = request.GET.get('images_only')

    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        if images_only:
            return HttpResponse('')
        images = paginator.page(paginator.num_pages)

    if images_only:
        return render(request,
                      'images/image/list_images.html',
                      {'section': 'images',
                       'images': images})

    return render(request,
                  'images/image/list.html',
                  {'section': 'images',
                   'images': images})

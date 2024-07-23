from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from .models import Course


class UserIsOwnerMixin:
    """Mixin to check if the user is the owner of the object."""

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class OwnerMixin:
    """Mixin to filter objects by owner."""

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin:
    """Mixin to set the owner of the object."""

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CourseMixin:
    """Mixin to configure Course model views."""
    model = Course
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')
    template_name = 'courses/manage/course/form.html'


class OwnerCourseMixin(OwnerMixin, CourseMixin):
    """Mixin to combine owner and course configuration."""


class OwnerCourseEditMixin(OwnerEditMixin, OwnerCourseMixin):
    """Mixin to combine owner, course configuration and editing."""


class ManageCourseListView(OwnerCourseMixin, ListView):
    """View to list courses managed by the owner."""
    template_name = 'courses/manage/course/list.html'


class CourseCreateView(OwnerCourseEditMixin, CreateView):
    """View to create a new course."""


class CourseUpdateView(UserIsOwnerMixin, OwnerCourseEditMixin, UpdateView):
    """View to update an existing course."""


class CourseDeleteView(UserIsOwnerMixin, OwnerCourseMixin, DeleteView):
    """View to delete a course."""
    template_name = 'courses/manage/course/delete.html'

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy


from .models import Course


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


class OwnerCourseMixin(
    OwnerMixin,
    CourseMixin,
    LoginRequiredMixin,
    PermissionRequiredMixin
):
    """Mixin to combine owner and course configuration."""


class OwnerCourseEditMixin(OwnerEditMixin, OwnerCourseMixin):
    """Mixin to combine owner, course configuration and editing."""


class ManageCourseListView(OwnerCourseMixin, ListView):
    """View to list courses managed by the owner."""
    template_name = 'courses/manage/course/list.html'
    permission_required = 'courses.view_course'


class CourseCreateView(OwnerCourseEditMixin, CreateView):
    """View to create a new course."""
    permission_required = 'courses.add_course'


class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    """View to update an existing course."""
    permission_required = 'courses.change_course'


class CourseDeleteView(OwnerCourseMixin, DeleteView):
    """View to delete a course."""
    template_name = 'courses/manage/course/delete.html'
    permission_required = 'courses.delete_course'

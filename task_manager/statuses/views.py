from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from task_manager.mixins import CheckSignInMixin, DeleteRelatedEntityMixin
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status


class ListStatusView(CheckSignInMixin, ListView):
    """All statuses"""
    model = Status
    template_name = 'statuses/list.html'
    context_object_name = 'statuses'


class CreateStatusView(CheckSignInMixin, SuccessMessageMixin, CreateView):
    """Create status"""
    model = Status
    form_class = StatusForm
    template_name = 'statuses/create.html'
    success_message = _('Статус успешно создан')
    success_url = reverse_lazy('statuses:list')


class UpdateStatusView(CheckSignInMixin, SuccessMessageMixin, UpdateView):
    """Update status"""
    model = Status
    form_class = StatusForm
    template_name = 'statuses/update.html'
    success_message = _('Статус успешно изменён')
    success_url = reverse_lazy('statuses:list')


class DeleteStatusView(CheckSignInMixin, DeleteRelatedEntityMixin, DeleteView):
    """Delete status"""
    model = Status
    template_name = 'statuses/delete.html'
    success_message = _('Статус успешно удалён')
    error_message = _('Невозможно удалить статус, потому что он используется')
    success_url = reverse_lazy('statuses:list')

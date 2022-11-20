from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from task_manager.statuses.models import Status


class StatusForm(ModelForm):
    """Form for status creation and update"""

    class Meta:
        model = Status
        fields = ['name']
        labels = {'name': _('Имя')}

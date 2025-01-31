import datetime

from django import forms
from django.core.exceptions import ValidationError
from django_flatpickr.widgets import DateTimePickerInput
from django.utils import timezone

from todo_list.models import Task, Tag


class TaskCreationForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                "rows": 3,
                "cols": 50,
                "placeholder": "Enter your task...",
            }
        ),
    )
    deadline = forms.DateTimeField(
        widget=DateTimePickerInput(
            attrs={
                'class': 'form-control w-25',
            }
        ),
        required=False,
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    def clean_deadline(self) -> datetime:
        user_deadline = self.cleaned_data["deadline"]
        current_time = timezone.now()
        if user_deadline <= current_time:
            raise ValidationError(f"Your deadline can't be earlier than {current_time}!")
        return user_deadline

    class Meta:
        model = Task
        fields = "__all__"

from django import forms
from django_flatpickr.widgets import DateTimePickerInput
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

    class Meta:
        model = Task
        fields = "__all__"

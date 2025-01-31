from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from todo_list.forms import TaskCreationForm
from todo_list.models import Task, Tag


class TaskListView(ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(CreateView):
    model = Task
    success_url = reverse_lazy("todo_list:home")
    form_class = TaskCreationForm


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskCreationForm
    success_url = reverse_lazy("todo_list:home")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:home")


class TagListView(ListView):
    model = Tag


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")


def toggle_status(request, pk: int):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("todo_list:home")
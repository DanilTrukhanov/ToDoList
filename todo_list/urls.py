from django.urls import path

from todo_list.views import TaskListView, TaskCreateView, TagListView, TaskUpdateView, toggle_status, TaskDeleteView, \
    TagCreateView, TagUpdateView

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("tasks/create/", TaskCreateView.as_view(), name="create-task"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="update-task"),
    path("tasks/<int:pk>/change-status/", toggle_status, name="change-status"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="delete-task"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
]

app_name = "todo_list"
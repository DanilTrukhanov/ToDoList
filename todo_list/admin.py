from django.contrib import admin

from todo_list.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

from django.test import TestCase
from django.urls import reverse

from todo_list.models import Task, Tag


class TestTaskList(TestCase):
    def test_get_task_list(self):
        response = self.client.get(reverse("todo_list:home"))
        self.assertEqual(response.status_code, 200)

    def test_task_list_order(self):
        Task.objects.create(
            content="TestTask1",
            is_done=True,
        )
        Task.objects.create(
            content="TestTask2",
            is_done=False,
        )

        response = self.client.get(reverse("todo_list:home"))

        actual_list = response.context.get("task_list")
        expected_list = Task.objects.all()

        self.assertEqual(list(actual_list), list(expected_list))

    def test_task_change_status_from_false_to_true(self):
        task = Task.objects.create(
            content="TestTask1",
            is_done=False,
        )
        self.client.get(reverse("todo_list:change-status", args=[task.id]))
        task.refresh_from_db()

        self.assertTrue(task.is_done)

    def test_task_change_status_from_true_to_false(self):
        task = Task.objects.create(
            content="TestTask1",
            is_done=True,
        )
        self.client.get(reverse("todo_list:change-status", args=[task.id]))
        task.refresh_from_db()

        self.assertFalse(task.is_done)


class TestTagList(TestCase):
    def test_get_tag_list(self):
        Tag.objects.create(name="important")
        Tag.objects.create(name="home")
        Tag.objects.create(name="work")

        response = self.client.get(reverse("todo_list:tag-list"))

        self.assertEqual(response.status_code, 200)

        actual_list = response.context.get("tag_list")
        expected_list = Tag.objects.all()

        self.assertEqual(list(actual_list), list(expected_list))

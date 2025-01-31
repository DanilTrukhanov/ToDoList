import datetime

from django.test import TestCase

from todo_list.forms import TaskCreationForm


INVALID_DEADLINE = datetime.datetime(
    year=2024,
    month=4,
    day=14,
    hour=12,
    minute=34
)

VALID_DEADLINE = datetime.datetime(
    year=2025,
    month=2,
    day=5,
    hour=11,
    minute=0
)

class TestTaskCreationForm(TestCase):

    @staticmethod
    def create_form(deadline):
        return TaskCreationForm(
            data={
                "content": "TestContent",
                "is_done": False,
                "deadline": deadline,
            }
        )

    def test_task_deadline_validation_with_deadline_in_past(self):
        self.assertFalse(
            self.create_form(INVALID_DEADLINE).is_valid()
        )

    def test_task_deadline_validation_with_valid_time(self):
        self.assertTrue(
            self.create_form(VALID_DEADLINE).is_valid()
        )

# Generated by Django 5.1.5 on 2025-01-31 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo_list", "0003_alter_task_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tag",
            options={"ordering": ["name"]},
        ),
    ]

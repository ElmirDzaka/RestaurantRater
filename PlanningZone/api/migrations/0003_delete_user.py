# Generated by Django 4.2.3 on 2023-07-19 23:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_rename_poll_room"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]

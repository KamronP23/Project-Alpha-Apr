# Generated by Django 4.1.4 on 2022-12-06 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="description",
            field=models.TextField(null=True),
        ),
    ]

# Generated by Django 5.0.4 on 2025-02-23 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wantmodel',
            name='subtitle',
        ),
    ]

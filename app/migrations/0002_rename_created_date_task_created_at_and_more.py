# Generated by Django 4.0.5 on 2022-06-14 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='updated_date',
            new_name='updated_at',
        ),
    ]

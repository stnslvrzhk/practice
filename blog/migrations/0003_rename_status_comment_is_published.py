# Generated by Django 3.2.3 on 2021-07-28 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='status',
            new_name='is_published',
        ),
    ]
# Generated by Django 2.1 on 2018-10-19 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0012_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='draft',
            new_name='is_draft',
        ),
    ]
# Generated by Django 2.1 on 2018-10-15 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0004_auto_20181015_0622'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover_image',
            field=models.ImageField(default=1, upload_to='media'),
            preserve_default=False,
        ),
    ]

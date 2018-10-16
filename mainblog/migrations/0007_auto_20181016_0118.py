# Generated by Django 2.1 on 2018-10-16 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0006_auto_20181015_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainblog.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='cover_image',
            field=models.ImageField(upload_to='cover_images'),
        ),
    ]

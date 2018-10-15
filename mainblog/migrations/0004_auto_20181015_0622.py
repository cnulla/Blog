# Generated by Django 2.1 on 2018-10-15 06:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0003_auto_20181012_0358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

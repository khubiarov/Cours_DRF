# Generated by Django 4.2.4 on 2023-08-09 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='url_video',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на видео'),
        ),
    ]

# Generated by Django 3.1 on 2021-02-14 21:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='info',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

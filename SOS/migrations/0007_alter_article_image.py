# Generated by Django 4.1.7 on 2023-03-31 23:42

import SOS.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SOS', '0006_alter_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to=SOS.models.upload_to, verbose_name='Image'),
        ),
    ]

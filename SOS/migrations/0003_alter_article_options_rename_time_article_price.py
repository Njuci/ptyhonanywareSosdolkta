# Generated by Django 4.1.7 on 2023-03-18 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SOS', '0002_article'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['id']},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='time',
            new_name='price',
        ),
    ]

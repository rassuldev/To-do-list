# Generated by Django 4.1 on 2022-09-06 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistapp', '0002_todolistitem_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistitem',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]

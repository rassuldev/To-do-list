# Generated by Django 4.1.1 on 2022-09-20 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolistapp', '0004_alter_todolistitem_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolistitem',
            options={'ordering': ['completed']},
        ),
    ]

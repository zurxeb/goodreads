# Generated by Django 4.2 on 2024-07-25 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_alter_book_cover_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cover_picture',
        ),
    ]

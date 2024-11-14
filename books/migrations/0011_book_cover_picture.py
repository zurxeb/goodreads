# Generated by Django 4.2 on 2024-07-25 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_remove_book_cover_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_picture',
            field=models.ImageField(default='cover_pictures/default-pictures.jpg', upload_to='cover_pictures'),
        ),
    ]

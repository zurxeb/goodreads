# Generated by Django 4.2 on 2024-07-20 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('male', 'Erkak'), ('female', 'Ayol')], default='male', max_length=10),
        ),
    ]

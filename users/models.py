from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(default='profile_pictures/male.jpg', upload_to='profile_pictures')
    gender = models.CharField(max_length=10, choices=(('male', 'Erkak'), ('female', 'Ayol')),default='male')


    def full_name(self):
        return f'{self.first_name} {self.last_name}'
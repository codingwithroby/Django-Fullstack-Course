from django.db import models
from django.contrib.auth.models import User


class UserImageExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(upload_to='user_images')

    def __str__(self):
        return f"{self.user.username} User's Image"

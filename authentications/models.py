from django.contrib.auth.models import User
from django.db import models
from .constants import GENDER_CHOICES,SPECIALTY_CHOICES

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    specialty = models.CharField(max_length=100, choices=SPECIALTY_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username
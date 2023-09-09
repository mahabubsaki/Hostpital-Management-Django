from django.db import models
from authentications.models import UserProfile

from .constants import ISSUE_CHOICES

# Create your models here.
class PatientDetails(models.Model):
    doctor = models.ManyToManyField(UserProfile)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.TextField()
    issue = models.CharField(choices=ISSUE_CHOICES,max_length=30)
    appointment_date = models.DateField()
    def __str__(self) -> str:
        return self.name
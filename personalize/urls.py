from django.urls import path
from .views import doctor_profile
urlpatterns = [
    path('',doctor_profile,name='profile'),
]
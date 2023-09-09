from django.urls import path
from .views import doctor_profile,delete_patient,update_patient
urlpatterns = [
    path('',doctor_profile,name='profile'),
    path('delete-patient/<int:id>',delete_patient,name='delete_patient'),
    path('update-patient/<int:id>',update_patient,name='update_patient')
]
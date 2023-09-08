from django.urls import path
from .views import home_page,add_patient,all_patients
urlpatterns = [
    path('',home_page,name='home'),
    path('add-patient/',add_patient,name="add_patient"),
    path('all-patients/',all_patients,name="all_patients")
]
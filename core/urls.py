from django.urls import path
from .views import home_page,add_patient,all_patients,custom_404,search_patients




urlpatterns = [
    path('',home_page,name='home'),
    path('add-patient/',add_patient,name="add_patient"),
    path('all-patients/',all_patients,name="all_patients"),
    path('all-patients/<str:patient_slug>/',all_patients,name="patients_by_issue"),
    path('search/',search_patients,name='search'),
    path('notfound/',custom_404,name='notfound')
]
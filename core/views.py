from django.shortcuts import render,redirect
from authentications.utils import get_current_user
from .forms import PatientDetailsForm
from .models import UserProfile 
from django.contrib import messages
# Create your views here.

def home_page(request):
    current_user = get_current_user(request)
    return render(request,'home-page.html',{'user':current_user})
def add_patient(request):
    if request.user.is_authenticated:
        current_user = get_current_user(request)
        if request.method == 'POST':
            form = PatientDetailsForm(request.POST)
            if form.is_valid():
                patient_details = form.save(commit=False) 
                doctor_profile = UserProfile.objects.get(user=request.user)
                patient_details.save()
                patient_details.doctor.set([doctor_profile])
                messages.success(request,"Patient added successfully to records")
                return redirect('add_patient')
        form = PatientDetailsForm()
        return render(request,'add-patient.html',{'form':form,'user':current_user})
    else:
        return redirect('login')
    
def all_patients(request):
    pass
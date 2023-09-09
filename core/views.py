from django.shortcuts import render,redirect
from authentications.utils import get_current_user
from .forms import PatientDetailsForm
from .models import UserProfile,PatientDetails
from django.contrib import messages
from .constants import ISSUE_LIST
from django.db.models import Q

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
                patient_details.doctor.add(doctor_profile)
                messages.success(request,"Patient added successfully to records")
                return redirect('add_patient')
        form = PatientDetailsForm()
        return render(request,'add-patient.html',{'form':form,'user':current_user})
    else:
        return redirect('login')
    
def all_patients(request,patient_slug=None):
    if request.user.is_authenticated:
        current_user = get_current_user(request)
        patients = PatientDetails.objects.all()
        if patient_slug:
            if patient_slug not in ISSUE_LIST:
                return redirect('notfound')
            patients = patients.filter(issue=patient_slug)
        return render(request,'all-patients.html',{'user':current_user,'patients':patients,'patient_slug':patient_slug})
    else:
        return redirect('login')
    
def search_patients(request):
    if request.user.is_authenticated:
        if 'keyword' in request.GET:
            current_user = get_current_user(request)
            keyword = request.GET['keyword']
            if keyword:
                patients = PatientDetails.objects.all().filter(Q(name__icontains=keyword))
            return render(request,'all-patients.html',{'user':current_user,'patients':patients,'search_value':keyword})
        else:
            return redirect('notfound')
    else:
        return redirect('login')

def custom_404(request, exception=None):
    if request.user.is_authenticated:
        current_user = get_current_user(request)
    else:
        current_user = None  
    return render(request, '404.html', status=404,context={'user':current_user})
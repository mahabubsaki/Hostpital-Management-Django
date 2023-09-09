from django.shortcuts import render,redirect
from authentications.utils import get_current_user
from core.models import PatientDetails
from core.forms import PatientDetailsForm
from django.contrib import messages
from datetime import datetime


# Create your views here.
def doctor_profile(request):
    if request.user.is_authenticated:
        current_user = get_current_user(request)
        patients = PatientDetails.objects.all().filter(doctor = current_user)
        return render(request,'profile.html',{'user':current_user,'patients':patients})
    else:
        return redirect('login')


def delete_patient(request,id):
    if request.user.is_authenticated:
        result = PatientDetails.objects.get(pk = id).delete()
        return redirect("profile")
    else:
        return redirect('login')
    
def update_patient(request,id):
    if request.user.is_authenticated:
        current_user = get_current_user(request)
        patient = PatientDetails.objects.get(pk = id)
        
        if request.method == 'POST':
          
            mutable_query_dict = request.POST.copy()

            date_string = request.POST.get('appointment_date')
            date_object = datetime.strptime(date_string, '%Y/%m/%d')
            formatted_date = date_object.strftime('%Y-%m-%d')
            mutable_query_dict['appointment_date'] = formatted_date
            form = PatientDetailsForm(mutable_query_dict,instance=patient)
            
            if form.is_valid():
                print('sd')
                form.save()
                messages.success(request,"Successfully edited the patient details")
                return redirect('profile')
        form = PatientDetailsForm(instance=patient)
        return render(request,'update-patient.html',{'form':form,'user':current_user})
    else:
        return redirect('login')
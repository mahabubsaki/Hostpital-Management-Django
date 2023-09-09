from django import forms
from .models import PatientDetails
from datetime import datetime

class PatientDetailsForm(forms.ModelForm):
    class Meta:
        model = PatientDetails
        fields = ['name','age','address','issue','appointment_date']
        today_date = datetime.now()
        formatted_date = today_date.strftime("%m/%d/%Y")
        widgets= {
            'name':forms.TextInput(attrs={'class':'block py-2.5 px-0 w-full text-md text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none  focus:outline-none focus:ring-0 focus:border-blue-600 peer','id':'name','placeholder':' '}),
            'age':forms.NumberInput(attrs={'class':'block py-2.5 px-0 w-full text-md text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none  focus:outline-none focus:ring-0 focus:border-blue-600 peer','id':'age','placeholder':' '}),
            'address':forms.TextInput(attrs={'class':'block py-2.5 px-0 w-full text-md text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none  focus:outline-none focus:ring-0 focus:border-blue-600 peer','id':'address','placeholder':' '}),
            'issue':forms.Select(attrs={'class':'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5','id':'issue'}),
            'appointment_date':forms.TextInput(attrs={'class':'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5','datepicker':'true','datepicker-autohide':'true','placeholder':'Select date','id':'appointment_date','datepicker-orientation':'bottom left','datepicker-buttons':'true','datepicker-format':'yyyy/mm/dd'})
        }
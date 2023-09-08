from django import forms
from django.contrib.auth.models import User
from .constants import GENDER_CHOICES,SPECIALTY_CHOICES
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'block py-2.5 px-0 w-full text-md text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none  focus:outline-none focus:ring-0 focus:border-blue-600 peer','id':'username','placeholder':' '}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'block py-2.5 px-0 w-full text-md text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none  focus:outline-none focus:ring-0 focus:border-blue-600 peer','id':'password','placeholder':' '}))

class RegistrationForm(forms.ModelForm):
    pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none','id':'pic'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'block py-2.5 px-0 w-full text-md text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none  focus:outline-none focus:ring-0 focus:border-blue-600 peer','id':'name','placeholder':' ',}))
    specialty = forms.ChoiceField(choices=SPECIALTY_CHOICES,widget=forms.Select(attrs={'class':'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5','id':'speciality'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.Select(attrs={'class':'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5','id':'gender'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets= {
            'username':forms.TextInput(attrs={'class':'block py-2.5 px-0 w-full text-md text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none  focus:outline-none focus:ring-0 focus:border-blue-600 peer','id':'username','placeholder':' '}),
            'email':forms.EmailInput(attrs={'class':'block py-2.5 px-0 w-full text-md text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none  focus:outline-none focus:ring-0 focus:border-blue-600 peer','id':'email','placeholder':' '}),
            'password':forms.PasswordInput(attrs={'class':'block py-2.5 px-0 w-full text-md text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none  focus:outline-none focus:ring-0 focus:border-blue-600 peer','id':'password','placeholder':' ',})
        }
    
    
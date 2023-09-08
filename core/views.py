from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request,'home-page.html')
def add_patient(request):
    pass
def all_patients(request):
    pass
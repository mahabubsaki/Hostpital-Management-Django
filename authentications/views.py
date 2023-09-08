from django.shortcuts import render,redirect
from .forms import LoginForm,RegistrationForm
from .models import UserProfile
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .utils import upload_image_to_imgbb

# Create your views here.

def auth_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username,password=password)
           
            if user is not None:
                login(request,user)
                messages.success(request,f'You are now logged in as {username}')
                return redirect('home')
            else:
                messages.error(request,"Invalid username or password.")
        else: 
           messages.error(request,"Invalid username or password.") 
    else:
        form = LoginForm()
    return render(request,'auth-login.html',{'form':form})



def auth_signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            img_file = form.cleaned_data['pic']
            img_link = upload_image_to_imgbb(img_file)
            if img_file:
                user = form.save(commit=False)
                password = form.cleaned_data['password']
                user.set_password(password)
                user.save()
                profile = UserProfile(user=user)
                profile.specialty = form.cleaned_data['specialty']
                profile.gender = form.cleaned_data['gender']
                profile.name = form.cleaned_data['name']
                profile.profile_picture = img_link
                profile.save()
                login(request, user)
                return redirect('home') 
            else:
                messages.error(request,"Error uploading image on Imgbb, Please try again or change the file")
                form = RegistrationForm()
        else:
            messages.error(request,"A username is already registered on this website")
            form = RegistrationForm()
    else:
        form = RegistrationForm()

    return render(request, 'auth-register.html', {'form': form})


def auth_logout(request):
    logout(request)
    return redirect('home')
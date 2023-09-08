from django.shortcuts import render,redirect
from .forms import LoginForm,RegistrationForm
from .models import UserProfile
from django.contrib.auth import login,authenticate
from django.contrib import messages

# Create your views here.

def auth_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
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
            # Create the User object
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # Create the UserProfile
            profile = UserProfile(user=user)
            profile.profile_picture = form.cleaned_data['profile_picture']
            profile.specialty = form.cleaned_data['specialty']
            profile.gender = form.cleaned_data['gender']
            profile.save()

            # Log in the user
            login(request, user)
            
            return redirect('home')  # Redirect to your home page

    else:
        form = RegistrationForm()

    return render(request, 'auth-register.html', {'form': form})
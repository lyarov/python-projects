from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from . import forms
# Create your views here.


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/login/')
        else:
            return redirect('/account/registration/')
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})


def edit_profile(request):
    user = request.user
    if request.method == "POST":
        form_user = forms.UserEditForm(request.POST, instance=user)
        if form_user.is_valid():
            form_user.save()
            return redirect('base')
        else:
            return redirect('edit_profile')
    else:
        form_user = forms.UserEditForm(instance=user)
          render(request, 'edit-profile.html', {'form_user': form_user})
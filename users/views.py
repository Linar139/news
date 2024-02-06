from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def userlogout(request):
	logout(request)
	return redirect('home')

@login_required
def profile(request):
    return render(request, 'profile.html')
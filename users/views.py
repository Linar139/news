from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			return redirect('home')
	else:
		form = UserRegisterForm()
	return render(request, 'register.html', {'form': form})
def userlogout(request):
	logout(request)
	return redirect('home')

@login_required
def profile(request):
    return render(request, 'profile.html')
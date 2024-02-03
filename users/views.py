from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Создан аккаунт {username}!')
			return redirect('home')
	else:
		form = UserRegisterForm()
	return render(request, 'register.html', {'form': form})
def userlogout(request):
	logout(request)
	messages.success(request, 'Вы вышли')
	return redirect('home')

def profile(request):
	return render(request, 'profile.html')

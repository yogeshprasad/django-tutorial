from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
def home(request):
	numbers = [1,2,3,4,5,6]
	name = "ram"
	args = {'name': name, 'numbers': numbers}
	return render(request, 'accounts/home.html', args)

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account')
	else:
		form = RegistrationForm()

		args = {'form': form}
		return render(request, 'accounts/reg_form.html', args)

# Create your views here.
def view_profile(request):
	args = {'user': request.user}
	return render(request, 'accounts/profile.html')

# Create your views here.
def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('/account/profile')

	else:
		form = EditProfileForm(instance=request.user)

		args = {'form': form}
		return render(request, 'accounts/edit_profile.html', args)
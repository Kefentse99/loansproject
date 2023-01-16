
from loanapplication.models import Customer
from machinelearning.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.contrib import messages
from .models import *

from .forms import  CreateUserForm ,ProfileForm
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group


@unauthenticated_user
def loginPage(request):

		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('homepage')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')

	
@allowed_users(allowed_roles=['teller','admin'])
def registerPage(request):	
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				user=form.save()				
				group = Group.objects.get(name='staff')
				user.groups.add(group)

				return redirect('bankstaff')
			

		context = {'form':form}
	
		return render(request, 'register.html', context)	



@allowed_users(allowed_roles=['teller','admin'])
def bankstaff (request):
        return render (request, 'bankstaff.html')

@allowed_users(allowed_roles=['teller','admin'])		
def account (request):
	Profile = request.user.profile
	form = ProfileForm(instance= Profile)

	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES,instance=Profile)
		if form.is_valid():
			form.save()


	context = {'form':form}
	
	return render (request, 'account.html', context)


@allowed_users(allowed_roles=['admin','teller'])
def emps(request):
        emps = Profile.objects.all()
        context = {'emps':emps}
        return render (request, 'bankstaff.html', context)

@admin_only
def bios(request,pk):
        bios = Profile.objects.get(id = pk)
        context = {'bios':bios}
        return render (request, 'bio.html', context)

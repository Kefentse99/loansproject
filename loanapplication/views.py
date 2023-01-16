from loanapplication.models import Customer
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from .forms import CustomerForm
from machinelearning.decorators import  *

from django.contrib import messages
from .models import *

from django.contrib.auth.models import Group


@login_required(login_url='login')
def homepage (request):
        return render (request, 'homepage.html')

@allowed_users(allowed_roles=['teller', 'admin'])
def customers (request):
    customers = Customer.objects.all()
    context= {'customers': customers}
    return render(request, 'datasumary.html', context)

@allowed_users(allowed_roles=['teller', 'admin' ])

def createForm (request):
    form= CustomerForm()

    if request.method == 'POST':
        form= CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('datasumary')

    context= {'form':form}
    return  render(request,'dataprocessing.html', context)



			
@allowed_users(allowed_roles=['teller', 'admin'])

def updateForm (request, pk):
    customer= Customer.objects.get( customerID = pk )
    form= CustomerForm(instance=customer)
    if request.method == 'POST':
        form= CustomerForm(request.POST , instance=customer)
        if form.is_valid():
            form.save()
            return redirect('datasumary')

    context= {'form':form} 
    return  render(request,'dataprocessing.html', context)


@allowed_users(allowed_roles=['teller','admin'])
def deleteCustomer(request,pk):
    customer= Customer.objects.get( customerID = pk )
    if request.method == 'POST':
        Customer.delete(customer)
        return redirect('datasumary')

    context= {'object':customer }
    return  render(request,'deletePage.html', context)



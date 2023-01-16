from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from machinelearning.models import Profile
import uuid

class Customer(models.Model):    
    customerID = models.UUIDField(default=uuid.uuid4 , unique=True, primary_key=True, editable=False)
    customerName= models.CharField( max_length = 200)
    creditrating= models.IntegerField()
    occupation=models.CharField(max_length=100)
    netIncome= models.IntegerField()
    def __str__(self):
        return self.customerName
    
class Branch(models.Model):
    branchID= models.AutoField(primary_key=True)
    branchName= models.CharField(max_length=100, null=False)
    swiftKey= models.CharField(max_length=200)
    address=models.CharField(max_length=100)

class LoanAgent(models.Model):
    employeeID= models.AutoField(primary_key=True, unique=True)
    employeeName= models.CharField( max_length = 200)
    branch = models.ManyToManyField(Branch, blank=True)

class Loaninfo(models.Model):
    loadID= models.UUIDField(default=uuid.uuid4 , unique=True, primary_key=True, editable=False)
    LOAN_TYPE=(
        ('car','Car Loan'),
        ('Home','Home Loan'),
        ('School','Student Loan'),
        ('personal', 'Personal Loan')
    )
    loanName=models.CharField(max_length=200)
    loanType= models.CharField(max_length=200, choices=LOAN_TYPE)
    loanDuration= models.CharField(max_length=20)
    loanAgent = models.ForeignKey(LoanAgent, on_delete=CASCADE)
    customer= models.ForeignKey(Customer , on_delete=CASCADE)
    branch = models.ForeignKey(Branch, on_delete=CASCADE)
    




    





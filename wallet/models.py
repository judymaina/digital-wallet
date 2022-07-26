
from email import message
from pyexpat import model
from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    address=models.TextField()
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)
    gender=models.CharField(max_length=10)
    age=models.PositiveSmallIntegerField()

class Account(models.Model):
    account_number=models.IntegerField(max_length=20)
    balance=models.IntegerField()
    account_name=models.CharField(max_length=20)

class Wallet(models.Model):
    pin=models.SmallIntegerField()
    amount=models.IntegerField()   
    date_created=models.DateTimeField()

class Transaction(models.Model):
    Date_time=models.DateTimeField()
    amount=models.IntegerField()
    customer_ID=models.CharField(max_length=12)

class Card(models.Model):
    name=models.CharField(max_length=12)
    number=models.IntegerField()
    expiry_date=models.DateTimeField()

class ThirdParty(models.Model):
    balance = models.IntegerField()
    transaction_cost = models. IntegerField()
    name = models.CharField(max_length=12)

class Notification(models.Model):
     date = models.DateTimeField()
     status = models.CharField(max_length=12)
     message = models.CharField(max_length=8)

class Receipt(models.Model):
    transaction = models.CharField(max_length=9)
    receipt_date= models.DateTimeField()
    total_Amount= models.IntegerField()

class Loan (models.Model) :
    interest_rate=models.IntegerField() 
    loan_type=models.CharField(max_length=9)
    loan_balance=models.IntegerField(max_length=16) 

class Reward (models.Model):
    gender=models.CharField(max_length=13)
    name=models.CharField(max_length=14)
    transaction=models.CharField(max_length=15)



from datetime import datetime
from email import message
from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20,null=True)
    address=models.TextField()
    email=models.EmailField()
    phone_number=models.CharField(max_length=15,null=True)
    gender=models.CharField(max_length=10)
    age=models.PositiveSmallIntegerField()

class Account(models.Model):
    account_number=models.IntegerField()
    account_name=models.CharField(max_length=20,null=True)
    account_type = models.CharField(max_length=20,null=True)
    account_balance = models.IntegerField()
    wallet = models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Account_wallet',null=True)

class Wallet(models.Model):
    pin=models.SmallIntegerField()
    amount=models.IntegerField()   
    date_created=models.DateTimeField(default=datetime.now)
    message = models.TextField(max_length=100, null=True)
    wallet = models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Transaction_wallet',null=True)
    transaction_description = models.CharField(max_length=9,null=True)
    transaction_charge = models.IntegerField(null=True)
    transaction_type = models.CharField(max_length=6,null=True)
    receipt = models.ForeignKey("Receipt",on_delete=models.CASCADE,related_name='Transaction_receipt',null=True)
    origin_account = models.ForeignKey("Wallet", on_delete=models.CASCADE,related_name='Transaction_origin',null=True)
    destination_account = models.ForeignKey("Wallet", on_delete=models.CASCADE,related_name='Transaction_destination',null=True)

class Transaction(models.Model):
    Date_time=models.DateTimeField(default=datetime.now)
    amount=models.IntegerField()
    customer_ID=models.CharField(max_length=12,null=True)

class Card(models.Model):
    name=models.CharField(max_length=12,null=True)
    expiry_date=models.DateTimeField(default=datetime.now)
    card_number= models.IntegerField()
    card_type= models.CharField(max_length=20,null=True)
    security_code = models.IntegerField(null=True)
    date_of_issue = models.DateTimeField(default=datetime.now)
    wallet= models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Card_wallet',null=True)
    account= models.ForeignKey("Account",on_delete=models.CASCADE,related_name='Card_account',null=True)
    issuer= models.CharField(max_length=10,null=True)

class ThirdParty(models.Model):
    balance = models.IntegerField()
    transaction_cost = models. IntegerField()
    name = models.CharField(max_length=12,null=True)
    account= models.ForeignKey("Account",on_delete=models.CASCADE,related_name='Thirdparty_account',null=True)
    currency = models.ForeignKey("Currency",on_delete=models.CASCADE,related_name='Thirdparty_currency',null=True)
    date_of_issue = models.DateTimeField(default=datetime.now)
    wallet= models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Thirdparty_wallet',null=True)
    issuer= models.CharField(max_length=20,null=True)

class Notification(models.Model):
     date = models.DateTimeField(default=datetime.now)
     status = models.CharField(max_length=12,null=True)
     message = models.CharField(max_length=8,null=True)
     
class Currency(models.Model):
    country= models.CharField(max_length=30,null=True)
    symbol= models.CharField(max_length=5,null=True)
    symbol= models.BigIntegerField()

class Receipt(models.Model):
    transaction = models.CharField(max_length=9,null=True)
    receipt_date= models.DateTimeField(default=datetime.now)
    total_Amount= models.IntegerField()
    receipt_number=models.IntegerField(null=True)

class Loan (models.Model) :
    interest_rate=models.IntegerField() 
    loan_type=models.CharField(max_length=9,null=True)
    loan_balance=models.IntegerField() 
    loan_id=models.IntegerField(null=True)
    guaranter=models.CharField(max_length=20,null=True)
    wallet=models.ForeignKey("wallet",on_delete=models.CASCADE,related_name="Loan_wallet",null=True)

class Reward (models.Model):
    gender=models.CharField(max_length=13,null=True)
    name=models.CharField(max_length=14,null=True)
    transaction=models.CharField(max_length=15,null=True)
    points=models.IntegerField(null=True)


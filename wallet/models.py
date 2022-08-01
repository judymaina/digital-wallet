
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
    account_number=models.IntegerField()
    account_name=models.CharField(max_length=20)
    account_type = models.CharField(max_length=20)
    account_balance = models.IntegerField()
    wallet = models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Account_wallet')

class Wallet(models.Model):
    pin=models.SmallIntegerField()
    amount=models.IntegerField()   
    date_created=models.DateTimeField()
    message = models.CharField(max_length=100)
    wallet = models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Transaction_wallet')
    transaction_description = models.CharField(max_length=9)
    transaction_charge = models.IntegerField()
    transaction_type = models.CharField(max_length=6)
    receipt = models.ForeignKey("Receipt",on_delete=models.CASCADE,related_name='Transaction_receipt')
    origin_account = models.ForeignKey("Wallet", on_delete=models.CASCADE,related_name='Transaction_origin')
    destination_account = models.ForeignKey("Wallet", on_delete=models.CASCADE,related_name='Transaction_destination')

class Transaction(models.Model):
    Date_time=models.DateTimeField()
    amount=models.IntegerField()
    customer_ID=models.CharField(max_length=12)

class Card(models.Model):
    name=models.CharField(max_length=12)
    expiry_date=models.DateTimeField()
    card_number= models.IntegerField()
    card_type= models.CharField(max_length=20)
    security_code = models.IntegerField()
    date_of_issue = models.DateTimeField()
    wallet= models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Card_wallet')
    account= models.ForeignKey("Account",on_delete=models.CASCADE,related_name='Card_account')
    issuer= models.CharField(max_length=10)

class ThirdParty(models.Model):
    balance = models.IntegerField()
    transaction_cost = models. IntegerField()
    name = models.CharField(max_length=12)
    account= models.ForeignKey("Account",on_delete=models.CASCADE,related_name='Thirdparty_account')
    currency = models.ForeignKey("Currency",on_delete=models.CASCADE,related_name='Thirdparty_currency')
    date_of_issue = models.DateTimeField()
    wallet= models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Thirdparty_wallet')
    issuer= models.CharField(max_length=20)

class Notification(models.Model):
     date = models.DateTimeField()
     status = models.CharField(max_length=12)
     message = models.CharField(max_length=8)
class Currency(models.Model):
    country= models.CharField(max_length=30)
    symbol= models.CharField(max_length=5)
    amount= models.BigIntegerField()

class Receipt(models.Model):
    transaction = models.CharField(max_length=9)
    receipt_date= models.DateTimeField()
    total_Amount= models.IntegerField()
    receipt_number=models.IntegerField()

class Loan (models.Model) :
    interest_rate=models.IntegerField() 
    loan_type=models.CharField(max_length=9)
    loan_balance=models.IntegerField() 
    loan_id=models.IntegerField()
    guaranter=models.CharField(max_length=20)
    wallet=models.ForeignKey("wallet",on_delete=models.CASCADE,related_name="Loan_wallet")

class Reward (models.Model):
    gender=models.CharField(max_length=13)
    name=models.CharField(max_length=14)
    transaction=models.CharField(max_length=15)
    points=models.IntegerField()


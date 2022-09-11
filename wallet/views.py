from locale import currency
from urllib import request
from django.shortcuts import render
from .import forms
from wallet.models import Account, Currency, Customer, Loan, Notification, Receipt, Reward, Transaction, Wallet
from .forms import CustomerRegistrationForm
from .forms import WalletRegistrationForm
from .forms import RecieptRegistrationForm
from .forms import LoanRegistrationForm
from .forms import AccountRegistrationForm
from .forms import CurrencyRegistrationForm
from .forms import NotificationRegistrationForm
from .forms import RewardRegistrationForm
from .forms import TransactionRegistrationForm




# Create your views here.
def register_customer(request):
    # form=CustomerRegistrationForm()
    # return render(request, "wallet/register_customer.html", {"form":form})
    if request.method =='POST':
       form = CustomerRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
    else:
        form = CustomerRegistrationForm()
    return render(request, "wallet/register_customer.html", {"form":form})


def register_wallet(request):
    # form = WalletRegistrationForm()
    # return render(request, "wallet/register_wallet.html", {"form":form})
    if request.method =='POST':
       form = WalletRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
    else:
        form = WalletRegistrationForm()
    return render(request, "wallet/register_wallet.html", {"form":form})


def register_reciept(request):
    # form = RecieptRegistrationForm()
    # return render(request, "wallet/register_reciept.html", {"form":form})
    if request.method =='POST':
       form = RecieptRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
    else:
        form = RecieptRegistrationForm()
    return render(request, "wallet/register_reciept.html", {"form":form})


def register_account(request):
    # form = AccountRegistrationForm()
    # return render(request, "wallet/register_account.html", {"form":form})
    if request.method =='POST':
       form = AccountRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
    else:
        form = AccountRegistrationForm()
    return render(request, "wallet/register_account.html", {"form":form})

def register_currency(request):
    # form = CurrencyRegistrationForm()
    # return render(request, "wallet/register_currency.html", {"form":form})
    if request.method =='POST':
       form = CurrencyRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
    else:
        form = CurrencyRegistrationForm()
    return render(request, "wallet/register_currency.html", {"form":form})


def register_notification(request):
    # form = NotificationRegistrationForm()
    # return render(request, "wallet/register_notification.html", {"form":form})
    if request.method =='POST':
       form = NotificationRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
    else:
        form = NotificationRegistrationForm()
    return render(request, "wallet/register_notification.html", {"form":form})


def register_loan(request):
    # form = LoanRegistrationForm()
    # return render(request, "wallet/register_loan.html", {"form":form})
    if request.method =='POST':
       form = LoanRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
    else:
        form = LoanRegistrationForm()
    return render(request, "wallet/register_loan.html", {"form":form})


def register_reward(request):
    # form = RewardRegistrationForm()
    # return render(request, "wallet/register_reward.html", {"form":form})
    if request.method =='POST':
       form = RewardRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
    else:
        form = RewardRegistrationForm()
    return render(request, "wallet/register_reward.html", {"form":form})


def register_transaction(request):
    # form = TransactionRegistrationForm()
    # return render(request, "wallet/register_transaction.html", {"form":form})
    if request.method =='POST':
       form = TransactionRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
    else:
        form = TransactionRegistrationForm()
    return render(request, "wallet/register_transaction.html", {"form":form})


# List
def list_customers(request):
    customers=Customer.objects.all()
    return render(request,"wallet/customers_list.html",{"customers":customers})

def list_wallets(request):
    wallets=Wallet.objects.all()
    return render(request,"wallet/wallets_list.html",{"wallets":wallets})
    
def list_reciepts(request):
    reciepts=Receipt.objects.all()
    return render(request,"wallet/reciepts_list.html",{"reciepts":reciepts})

def list_accounts(request):
    accounts=Account.objects.all()
    return render(request,"wallet/accounts_list.html",{"accounts":accounts})

def list_currencys(request):
    currencys=Currency.objects.all()
    return render(request,"wallet/currencys_list.html",{"currencys":currencys})

def list_notifications(request):
    notifications=Notification.objects.all()
    return render(request,"wallet/notifications_list.html",{"notifications":notifications})

def list_loans(request):
    loans=Loan.objects.all()
    return render(request,"wallet/loans_list.html",{"loans":loans})

def list_rewards(request):
    rewards=Reward.objects.all()
    return render(request,"wallet/rewards_list.html",{"rewards":rewards})

def list_transactions(request):
    transactions=Transaction.objects.all()
    return render(request,"wallet/transactions_list.html",{"transactions":transactions})


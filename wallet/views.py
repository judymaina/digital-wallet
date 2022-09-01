from django.shortcuts import render
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
    form=CustomerRegistrationForm()
    return render(request, "wallet/register_customer.html", {"form":form})

def register_wallet(request):
    form = WalletRegistrationForm()
    return render(request, "wallet/register_wallet.html", {"form":form})

def register_reciept(request):
    form = RecieptRegistrationForm()
    return render(request, "wallet/register_reciept.html", {"form":form})

def register_account(request):
    form = AccountRegistrationForm()
    return render(request, "wallet/register_account.html", {"form":form})

def register_currency(request):
    form = CurrencyRegistrationForm()
    return render(request, "wallet/register_currency.html", {"form":form})

def register_notification(request):
    form = NotificationRegistrationForm()
    return render(request, "wallet/register_notification.html", {"form":form})

def register_loan(request):
    form = LoanRegistrationForm()
    return render(request, "wallet/register_loan.html", {"form":form})

def register_reward(request):
    form = RewardRegistrationForm()
    return render(request, "wallet/register_reward.html", {"form":form})

def register_transaction(request):
    form = TransactionRegistrationForm()
    return render(request, "wallet/register_transaction.html", {"form":form})





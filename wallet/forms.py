from django import forms
from django.forms import ModelForm
from .models import Account,Customer, Loan, Notification, Receipt, Reward, Wallet, Transaction


class CustomerRegistrationForm(forms.ModelForm):
    class Meta: #inherits from the parent and overrides
        model = Customer
        fields ="__all__"

class WalletRegistrationForm(forms.ModelForm):
    class Meta: #inherits from the parent and overrides
        model = Wallet
        fields = "__all__"  

class RecieptRegistrationForm(forms.ModelForm):
    class Meta: #inherits from the parent and overrides
        model = Receipt
        fields = "__all__"  

class NotificationRegistrationForm(forms.ModelForm):
    class Meta: #inherits from the parent and overrides
        model = Notification
        fields = "__all__"  

class LoanRegistrationForm(forms.ModelForm):
    class Meta: #inherits from the parent and overrides
        model = Loan
        fields = "__all__"  

class AccountRegistrationForm(forms.ModelForm):
    class Meta: #inherits from the parent and overrides
        model = Account
        fields = "__all__"  

class RewardRegistrationForm(forms.ModelForm):
    class Meta: #inherits from the parent and overrides
        model = Reward
        fields = "__all__"  

# class CurrencyRegistrationForm(forms.ModelForm):
#     class Meta: #inherits from the parent and overrides
#         model = Currency
#         fields = "__all__"  

class TransactionRegistrationForm(forms.ModelForm):
    class Meta: #inherits from the parent and overrides
        model = Transaction
        fields = "__all__"  


from django.contrib import admin

# Register your models here.

from .models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet

class CustomerAdmin(admin.ModelAdmin):
     list_display=('first_name','last_name','age')
     search_fields=('first_name','last_name','age')
admin.site.register(Customer,CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
     list_display=('amount','date_created','message')
     search_fields=('amount','date_created','message')
admin.site.register(Wallet,WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
     list_display=('account_name','account_type','account_balance')
     search_fields=('account_name','account_type','account_balance')
admin.site.register(Account,AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
     list_display=('Date_time','amount','customer_ID')
     search_fields=('Date_time','amount','customer_ID')
admin.site.register(Transaction,TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
     list_display=('wallet','card_number','expiry_date')
     search_fields=('wallet','card_number','expiry_date')
admin.site.register(Card,CardAdmin)

class RecieptAdmin(admin.ModelAdmin):
     list_display=('receipt_number','receipt_date','total_Amount')
     search_fields=('receipt_number','receipt_date','total_Amount')
admin.site.register(Receipt,RecieptAdmin)

class ThirdPartyAdmin(admin.ModelAdmin):
     list_display=('balance','transaction_cost','name')
     search_fields=('balance','transaction_cost','name')
admin.site.register(ThirdParty,ThirdPartyAdmin)

class NotificationAdmin(admin.ModelAdmin):
     list_display=('date','status','message')
     search_fields=('date','status','message')
admin.site.register(Notification,NotificationAdmin)

class LoanAdmin(admin.ModelAdmin):
     list_display=('loan_type','loan_balance','loan_id')
     search_fields=('loan_type','loan_balance','loan_id')
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
     list_display=('gender','transaction','name')
     search_fields=('balance','transaction_cost','name')
admin.site.register(Reward,RewardAdmin)

class Currencydmin(admin.ModelAdmin):
     list_display=('country','symbol','symbol')
     search_fields=('country','symbol','symbol')
admin.site.register(Currency,Currencydmin)








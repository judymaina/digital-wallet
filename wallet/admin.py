from django.contrib import admin

# Register your models here.

from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet

class CustomerAdmin(admin.ModelAdmin):
     list_display=('first_name','last_name','age')
     search_fields=('first_name','last_name','age')
admin.site.register(Customer,CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
     list_display=('balance','date_created')
     search_fields=('balance','date_created')
admin.site.register(Wallet,WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
     list_display=('account_name','account_type','balance')
     search_fields=('account_name','account_type','balance')
admin.site.register(Account,AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
     list_display=('date_time','transaction_amount','wallet')
     search_fields=('date_time','transaction_amount','wallet')
admin.site.register(Transaction,TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
     list_display=('wallet','cardholder_number','expiry_date')
     search_fields=('wallet','cardholder_number','expiry_date')
admin.site.register(Card,CardAdmin)

class RecieptAdmin(admin.ModelAdmin):
     list_display=('receipt_date','total_Amount')
     search_fields=('receipt_date','total_Amount')
admin.site.register(Receipt,RecieptAdmin)

class ThirdPartyAdmin(admin.ModelAdmin):
     list_display=('balance','transaction_cost','name')
     search_fields=('balance','transaction_cost','name')
admin.site.register(ThirdParty,ThirdPartyAdmin)

class NotificationAdmin(admin.ModelAdmin):
     list_display=('date','status')
     search_fields=('date','status',)
admin.site.register(Notification,NotificationAdmin)

class LoanAdmin(admin.ModelAdmin):
     list_display=('loan_balance','pay_due_date')
     search_fields=('loan_balance','pay_due_date')
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
     list_display=('gender','transaction')
     search_fields=('balance','transaction_cost')
admin.site.register(Reward,RewardAdmin)








from django.urls import path
from .views import register_customer
from .views import register_wallet
from .views import register_account
from .views import register_transaction
from .views import register_loan
from .views import register_currency
from .views import register_reciept
from .views import register_reward
from .views import register_notification
from .import views



urlpatterns=[
path("register/",register_customer,name="registration"),
path("regwallet/", register_wallet, name="registration"),
path("regaccount/",register_account,name="registration"),
path("regloan/",register_loan,name="registration"),
path("regtranscation/",register_transaction,name="registration"),
path("regnotification/",register_notification,name="registration"),
path("regcurrency/",register_currency,name="registration"),
path("regreciept/",register_reciept,name="registration"),
path("regreward/",register_reward,name="registration"),
path("regtransaction/",register_transaction,name="registration"),

path("customers/",views.list_customers,name="customers_lists"),
path("wallets/",views.list_wallets,name="wallets_lists"),
path("accounts/",views.list_accounts,name="accounts_lists"),
path("reciepts/",views.list_reciepts,name="reciepts_lists"),
path("notifications/",views.list_notifications,name="notifications_lists"),
path("rewards/",views.list_rewards,name="rewards_lists"),
path("currencys/",views.list_currencys,name="currencys_lists"),
path("loans/",views.list_loans,name="loans_lists"),
path("transactions/",views.list_transactions,name="transactions_lists"),
]
    
from django.urls import path
from .views import AccountDetails, AddTransaction


urlpatterns = [
    path("",AccountDetails, name="transaction"),
    path("transaction",AddTransaction, name="transaction")

]

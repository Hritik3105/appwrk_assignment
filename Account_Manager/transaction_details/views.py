from django.shortcuts import render, redirect
from .models import DailyTransaction


# login to show transaction
def AccountDetails(request):

    transaction_details = DailyTransaction.objects.all().order_by("-id")
    return render(request, "home.html", {"data": transaction_details})


# Logic to add transaction
def AddTransaction(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        tran_type = request.POST.get("tran_type")
        decimal_amount = float(amount)
        tran_obj = DailyTransaction.objects.all().last()

        if tran_type == "debit":
            if tran_obj:
                main_balance = float(tran_obj.balance) - decimal_amount
            else:
                main_balance = decimal_amount
            DailyTransaction.objects.create(
                balance=float(main_balance),
                description=description,
                is_debit=decimal_amount,
            )
        else:
            if tran_obj:
                main_balance = float(tran_obj.balance) + decimal_amount
            else:
                main_balance = decimal_amount
            DailyTransaction.objects.create(
                balance=float(main_balance),
                description=description,
                is_credit=decimal_amount,
            )
        return redirect("transaction")
    return render(request, "add_transaction.html")

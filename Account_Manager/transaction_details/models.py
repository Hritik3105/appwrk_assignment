from django.db import models

# Create your models here.
class DailyTransaction(models.Model):
    description = models.CharField(max_length=200,blank= True, null =True)
    is_credit = models.DecimalField(default=0.00,decimal_places=2, max_digits=10)
    is_debit = models.DecimalField(default=0.00,decimal_places=2, max_digits=10)
    date = models.DateField(auto_now=True)
    balance =models.DecimalField(default=0.00,decimal_places=2, max_digits=10)
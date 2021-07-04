from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class MyUser(AbstractUser):
    account_number=models.CharField(max_length=16,unique=True)
    options=(("savings","savings"),
             ("current","current"),
             ("credit","credit"))
    account_type=models.CharField(max_length=20,choices=options,default="savings")
    balance=models.FloatField()
    phone=models.CharField(max_length=12)
class Transactions(models.Model):
    from_account_number=models.CharField(max_length=16)
    to_account_number=models.CharField(max_length=16)
    amount=models.FloatField()
    notes=models.CharField(max_length=150)
    date=models.DateField(auto_now=True)
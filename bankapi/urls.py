from django.urls import path
from .views import AccountCreation,FundTransfer

urlpatterns = [
    path("register",AccountCreation.as_view(),name="books"),
    path("transfer",FundTransfer.as_view(),name="fundtransfer")

]
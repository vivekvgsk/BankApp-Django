from django.urls import path
from .views import AccountCreateView,SigninView,BalanceView,FundTransferView,PaymentHistory,TransactionFilterView,SignOutView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path("",TemplateView.as_view(template_name="loginregisterbase.html"),name="index"),
    path("login",SigninView.as_view(),name="signin"),
    path("register",AccountCreateView.as_view(),name="register"),
    path("home",login_required(TemplateView.as_view(template_name="home.html"),login_url='signin'),name="home"),
    path("balance",BalanceView.as_view(),name="balance"),
    path("transactions",FundTransferView.as_view(),name="transactions"),
    path("paymenthistory",PaymentHistory.as_view(),name="paymenthistory"),
    path("filter",TransactionFilterView.as_view(),name="filter"),
    path("logout",SignOutView.as_view(),name="signout")
]

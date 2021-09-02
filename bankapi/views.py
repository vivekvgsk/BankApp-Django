from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import AccountCreationSeriallizer,TransactionSerializer
from rest_framework.response import Response
from bank.models import MyUser,Transactions
# Create your views here.
class AccountCreation(APIView):
    def get(self,request):
        customer=MyUser.objects.all()
        serializer=AccountCreationSeriallizer(customer,many=True)
        return Response(serializer.data,status=400)

    def post(self,request):
        serializer=AccountCreationSeriallizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        else:
            return Response(serializer.errors,status=400)
class FundTransfer(APIView):
    def get(self,request):
        transactions=Transactions.objects.all()
        serializer=TransactionSerializer(transactions,many=True)
        return Response(serializer.data,status=200)





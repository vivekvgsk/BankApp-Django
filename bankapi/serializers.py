from rest_framework import serializers
from bank.models import MyUser
from django.contrib.auth.models import AbstractUser

class AccountCreationSeriallizer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=fields=["first_name","username","email","account_number",
                        "account_type","balance","phone"]
class TransactionSerializer(serializers.Serializer):
    from_account_number=serializers.CharField()
    to_account_number=serializers.CharField()

    amount=serializers.FloatField()
    notes=serializers.CharField()







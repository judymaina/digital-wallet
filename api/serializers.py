from rest_framework import serializers
from wallet.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class meta:
        model=Customer
        fields=("firstname","email","age","address",)

from rest_framework import serializers
from library.models.Loan import Loan

class LoanSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Loan
        fields = '__all__'
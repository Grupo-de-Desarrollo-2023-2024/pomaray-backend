from rest_framework import viewsets

from library.models.Loan import Loan
from library.serializers.Loan import LoanSerializer


# Create your views here.


class LoanView(viewsets.ModelViewSet):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()

from rest_framework import status
from rest_framework.response import Response
from api.serializer import CustomerSerializer
from ..models import Customers

class CustomerService:
    def getAll_customers(self):
        return Customers.objects.all()
    def get_customers_by_id(self,id):
        return Customers.objects.get(customerid = id)
    def update_customers_by_id(self,id, request):
        customer = Customers.objects.get(customerid = id)
        serializer = CustomerSerializer(customer, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def filtrarComienzaCon(self,letra):
        return Customers.objects.filter(contactname__startswith=letra)
    

        
from rest_framework import status
from rest_framework.response import Response
from api.serializer import CustomerSerializer
from ..models import Products

class punto1Service:
    def getProductsFilter(self,supplier,category):
        Products.objects.filter(categoryid=category).filter(supplierid=supplier)#ver si funciona        
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from api.models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'
        
class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = '__all__'

class TerritoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Territories
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
        
#uso esto para que pueda hacer referencia a la foreign key del reportsto
class EmployeeNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
        
class EmployeeSerializer(serializers.ModelSerializer):
    reportsto = EmployeeNestedSerializer(many=False,required=False)
    class Meta:
        model = Employees
        fields = '__all__'

class ShipperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shippers
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    supplierid = SuppliersSerializer(many=False,required=False)
    categoryid = CategorySerializer(many=False,required=False)
    class Meta:
        model = Products
        fields = '__all__'
        
class OrderdetailsSerializer(serializers.ModelSerializer):
    productid = ProductSerializer(many=False,required=False)
    orderid = OrderSerializer(many=False,required=False)
    class Meta:
        model = Orderdetails
        fields = '__all__'
    
class ejemplo1Serializer(serializers.Serializer):
    id = serializers.IntegerField()
    nombre = serializers.CharField()
    apellido = serializers.CharField()
    reportsto = EmployeeSerializer(many=False,required=False)
    nacimiento = serializers.DateTimeField()
    salarioanterior = serializers.IntegerField()
    salario = serializers.IntegerField()
    
class Ejemplo2Serializer(serializers.Serializer):
    id = serializers.IntegerField()
    nombre = serializers.CharField()
    apellido = serializers.CharField()
    birthdate = serializers.DateTimeField()
    country = serializers.CharField()
    newCountry = serializers.CharField()
    
class Punto1Serializer(serializers.Serializer):
    ProductId = serializers.IntegerField()
    ProductName = serializers.CharField()
    stockFuturo = serializers.IntegerField()
    UnitPrice = serializers.IntegerField()
    
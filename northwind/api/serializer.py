from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from api.models import *

class SerializerPadre(ModelSerializer):
    class Meta:
        fields = '__all__'

class CustomerSerializer(SerializerPadre):
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
    customerid = CustomerSerializer(many=False,required=False)
    employeeid = EmployeeSerializer(many=False,required=False)
    shipvia = ShipperSerializer(many=False,required=False)
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
    class Meta:
        model = Orderdetails
        fields = '__all__'
    
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import (
    Orderdetails, Suppliers, Categories, 
    Employees, Orders, Products, Customers
)
from .serializer import (
    OrderdetailsSerializer, SuppliersSerializer,CustomerSerializer,
    CategorySerializer, EmployeeSerializer, OrderSerializer, ProductSerializer
)
from .serializer import CustomerSerializer
from api.services.CustomerService import CustomerService

customerservice = CustomerService()

# Create your views here.
"""@api_view(['GET'])
def Customers_all(request):
    customers = customerservice.getAll_customers()
    serializados = CustomerSerializer(customers,many = True)
    return Response(serializados.data)
    
    

@api_view(['GET', 'PUT', 'DELETE'])
def Customers_id(request, pk):
    if request.method == 'GET':
        customer = customerservice.get_customers_by_id(pk)
        serialized = CustomerSerializer(customer)
        return Response(serialized.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        return customerservice.update_customers_by_id(pk, request)
        
        
    if request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_200_OK)"""
@api_view(['GET', 'POST'])
def Customers_all(request):
    if request.method == 'GET':
        customers = Customers.objects.all()
        serialized = CustomerSerializer(customers, many=True)
        return Response(serialized.data)
    elif request.method == 'POST':
        serialized = CustomerSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_200_OK)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Customers_id(request, pk):
    try:
        customer = Customers.objects.get(customerid=pk)
    except Customers.DoesNotExist:
        return Response({"message": "No existe el cliente"}, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        serialized = CustomerSerializer(customer)
        return Response(serialized.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        request.data['customerid'] = pk
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_200_OK)
    

@api_view(['GET'])
def get_by_start_letter(request):
    letra = request.query_params.get('letra')
    customers  = customerservice.filtrarComienzaCon(letra)
    serializados = CustomerSerializer(customers,many = True)
    return Response(serializados.data)


@api_view(['GET', 'POST'])
def suppliers(request):
    if request.method == 'GET':
        suppliers = Suppliers.objects.all()
        serialized = SuppliersSerializer(suppliers, many=True)
        return Response(serialized.data)
    elif request.method == 'POST':
        serialized = SuppliersSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def suppliers_id(request, pk):
    try:
        supplier = Suppliers.objects.get(supplierid=pk)
    except Suppliers.DoesNotExist:
        return Response({"message": "No existe el proveedor"}, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        serialized = SuppliersSerializer(supplier)
        return Response(serialized.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        request.data['supplierid'] = pk
        serializer = SuppliersSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        supplier.delete()
        return Response(status=status.HTTP_200_OK)

# Categories (puedes replicar este patrón para las demás clases)
@api_view(['GET', 'POST'])
def categories(request):
    if request.method == 'GET':
        categories = Categories.objects.all()
        serialized = CategorySerializer(categories, many=True)
        return Response(serialized.data)
    elif request.method == 'POST':
        serialized = CategorySerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def categories_id(request, pk):
    try:
        category = Categories.objects.get(categoryid=pk)
    except Categories.DoesNotExist:
        return Response({"message": "No existe la categoría"}, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        serialized = CategorySerializer(category)
        return Response(serialized.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        request.data['categoryid'] = pk
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_200_OK)
    
@api_view(['GET', 'POST'])
def products(request):
    if request.method == 'GET':
        products = Products.objects.all()
        serialized = ProductSerializer(products, many=True)
        return Response(serialized.data)
    elif request.method == 'POST':
        serialized = ProductSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def products_id(request, pk):
    try:
        product = Products.objects.get(productid=pk)
    except Products.DoesNotExist:
        return Response({"message": "No existe el producto"}, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        serialized = ProductSerializer(product)
        return Response(serialized.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        request.data['productid'] = pk
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_200_OK)

# Orders
@api_view(['GET', 'POST'])
def orders(request):
    if request.method == 'GET':
        orders = Orders.objects.all()
        serialized = OrderSerializer(orders, many=True)
        return Response(serialized.data)
    elif request.method == 'POST':
        serialized = OrderSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def orders_id(request, pk):
    try:
        order = Orders.objects.get(orderid=pk)
    except Orders.DoesNotExist:
        return Response({"message": "No existe la orden"}, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        serialized = OrderSerializer(order)
        return Response(serialized.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        request.data['orderid'] = pk
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_200_OK)

# Order Details
@api_view(['GET', 'POST'])
def orderdetails(request):
    if request.method == 'GET':
        orderdetails = Orderdetails.objects.all()
        serialized = OrderdetailsSerializer(orderdetails, many=True)
        return Response(serialized.data)
    elif request.method == 'POST':
        serialized = OrderdetailsSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def orderdetails_id(request, pk):
    try:
        orderdetail = Orderdetails.objects.get(orderdetailid=pk)
    except Orderdetails.DoesNotExist:
        return Response({"message": "No existe el detalle de orden"}, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        serialized = OrderdetailsSerializer(orderdetail)
        return Response(serialized.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        request.data['orderdetailid'] = pk
        serializer = OrderdetailsSerializer(orderdetail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        orderdetail.delete()
        return Response(status=status.HTTP_200_OK)

# Employees
@api_view(['GET', 'POST'])
def employees(request):
    if request.method == 'GET':
        employees = Employees.objects.all()
        serialized = EmployeeSerializer(employees, many=True)
        return Response(serialized.data)
    elif request.method == 'POST':
        serialized = EmployeeSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def employees_id(request, pk):
    try:
        employee = Employees.objects.get(employeeid=pk)
    except Employees.DoesNotExist:
        return Response({"message": "No existe el empleado"}, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        serialized = EmployeeSerializer(employee)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
"""def punto1(request):
    
    
    #mostrar los clientes que su apellido comiencen con la letra "a" y la condicion iva sea responsable incripto, mostrar su apellido, id y descripcion condicion iva
    if request.method == 'GET':
        mayorQue = int(request.query_params.get('mayorQue'))#recibe el parametro desde el postman
        letra = request.query_params.get('letra')
        #clientes = Clientes.objects.all().values("cod_cliente")#SELECT COD_CLIENTE FROM CLIENTES con serializador personalizado
        #clientes = Clientes.objects.filter(apellido__startswith=letra).filter(cod_condicion_iva__descripcion="RESPONSABLE INSCRIPTO")#SELECT COD_CLIENTE FROM CLIENTES where apellido starts a
        #fechas exclude(date__gt = datetime.date(2005-1-3) EL GT ES GREATER THAN
        clientes = service.filtroPunto1(letra=letra,condicion="RESPONSABLE INSCRIPTO")
        resultados = []
        for cliente in clientes:
            if cliente.esMayor(mayorQue):
                service.update_telefono(id=cliente.cod_cliente, telefono=request.data['telefono'])
                resultado = { #creas un diccionario para cambiar de nombre los atributos o hacer una estructura para que se muestren los datos
                            "id":cliente.cod_cliente,
                            "apellido":cliente.apellido,
                            "nombre":cliente.nombre,
                            "telefono":cliente.telefono,
                            "telefonoNuevo":request.data['telefono'],
                            "descripcionIva":cliente.cod_condicion_iva.descripcion #descripcion iva
                            }
                
                resultados.append(resultado)
        serializados = Punto1Serializer(resultados, many=True)#creas un serializador nuevo para que tenga solo los atributos que le queres pasar, en este caso "cod_cliente","nombre","apellido"
        return Response(serializados.data)"""

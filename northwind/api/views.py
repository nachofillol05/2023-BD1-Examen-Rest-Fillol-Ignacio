import datetime
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import (
    Orderdetails, Shippers, Suppliers, Categories, 
    Employees, Orders, Products, Customers
)
from .serializer import (
    OrderdetailsSerializer, SuppliersSerializer,CustomerSerializer,
    CategorySerializer, EmployeeSerializer, OrderSerializer, ProductSerializer,
    Punto1Serializer,Ejemplo2Serializer,ejemplo1Serializer
)
from .serializer import CustomerSerializer
from api.services.CustomerService import CustomerService
from api.services.punto1Service import punto1Service

punto1service = punto1Service()
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
def orderdetails_id(request, pk,pk2):
    try:
        orderdetail = Orderdetails.objects.get(orderid=pk,productid=pk2)
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
@api_view(['GET'])
def ejemplo1(request):
    if request.method == 'GET':
        fecha = request.query_params.get('mayorquefecha')
        try:
            fecha = datetime.datetime.strptime(fecha, '%Y-%m-%d').date()
        except ValueError:
            fecha = None
        letra = request.query_params.get('letra')
        employees = Employees.objects.filter(birthdate__lt=fecha).filter(lastname__contains = letra).filter(reportsto__lastname__contains = letra)
        resultados = []
        for employee in employees:
            
            resultado = { 
                        "id":employee.employeeid,
                        "nombre": employee.firstname,
                        "apellido":employee.lastname,
                        "nacimiento":employee.birthdate,
                        "salarioanterior":employee.salary,
                        "salario":request.data['salario']
                        }
            print('trabo1')
            resultados.append(resultado)
            employee.salary = float(request.data['salario'])
            print(employee.salary)
            try:
                print("Antes de guardar el empleado")
                employee.save()
                print("Después de guardar el empleado")
            except Exception as e:
                print(f"Error al guardar el empleado: {e}")
           
        serializados = ejemplo1Serializer(resultados, many=True)#creas un serializador nuevo para que tenga solo los atributos que le queres pasar, en este caso "cod_cliente","nombre","apellido"
        return Response(serializados.data)
@api_view(['GET'])
def hola(request):
    employees = Employees.objects.filter(birthdate__lt = datetime.date(1950,1,3))
    serialized = EmployeeSerializer(employees, many=True)
    return Response(serialized.data)


@api_view(["GET"])
def ejemplo2(request):
    letra = request.query_params.get("letter")
    year = request.query_params.get("year")

    empleadosFiltrados = Employees.objects.filter(firstnameicontains = letra, birthdateyear__gte = year)
    resultados = []
    for e in empleadosFiltrados:
        resultado = {
            "id" : e.employeeid,
            "nombre" : e.firstname,
            "apellido" : e.lastname,
            "birthdate" : e.birthdate,
            "country" : e.country,
            "newCountry" : request.query_params.get("newCountry"),
        }
        resultados.append(resultado)
        e.country = request.query_params.get("newCountry")
        e.save()

    serializados = Ejemplo2Serializer(resultados, many=True)
    return Response(serializados.data)

@api_view(["GET"])
def punto1(request):
    supplierid = request.query_params.get("supplierid")
    categoryid = request.query_params.get("categoryid")
    stockmin = int(request.query_params.get("stockmin"))

    #productos = punto1service.getProductsFilter(supplierid,categoryid)
    productos = Products.objects.filter(categoryid=categoryid).filter(supplierid=supplierid)
    try:
        supplier = Suppliers.objects.get(supplierid= supplierid)
        category = Categories.objects.get(categoryid= categoryid)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print(supplierid,categoryid)
    print(productos)
    if productos:
        resultados = []
        for producto in productos:
            stockfuturo = producto.stockFuturo()
            print('calc',stockfuturo)
            if stockfuturo>stockmin and producto.discontinued != 1:
                
                resultado = {
                "ProductId" : producto.productid,
                "ProductName" : producto.productname,
                "stockFuturo" : stockfuturo,
                "UnitPrice" : producto.unitprice
            }
                resultados.append(resultado)
                
        """for i in range(len(resultado)-1):
            for k in range(len(resultado)-i-1):
                if resultados[k].stockFuturo<resultados[k+1].stockFuturo:
                    resultados[k], resultados[k+1] = resultados[k+1],resultados[k]"""
        serializados = Punto1Serializer(resultados, many=True)
        return Response(serializados.data,status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)
        
            
            
            
@api_view(["POST"])
def punto2(request):
    supplierid = request.query_params.get("supplierid")
    categoryid = request.query_params.get("categoryid")
    stockmin = int(request.query_params.get("stockmin"))
    
    
    customerid = request.data["CustomerID"]
    employeeid = request.data["EmployeeID"]
    shipperid = request.data["ShipperID"]
    
    try:
        supplier = Suppliers.objects.get(supplierid= supplierid)
        category = Categories.objects.get(categoryid= categoryid)
        ShipperID = Shippers.objects.get(shipperid= shipperid)
        EmployeeID = Employees.objects.get(employeeid= employeeid)
        CustomerID = Customers.objects.get(customerid= customerid)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    productos = Products.objects.filter(categoryid=categoryid).filter(supplierid=supplierid)
    print(supplierid,categoryid)
    if productos != None:
        resultados = []
        for producto in productos:
            stockfuturo = producto.stockFuturo()
            if stockfuturo<stockmin:
                resultados.append(producto)
                
            
            cantidad = stockfuturo - stockmin
            print(cantidad)
            customer = Customers.objects.get(customerid=customerid)
            lastOrder = Orders.objects.all()
            last = len(lastOrder)
            neworder =  Orders(last,customer.customerid,employeeid,datetime.datetime.now(),datetime.datetime.now(),datetime.datetime.now(),shipperid,0,customer.address,customer.city,customer.region,customer.postalcode,customer.country)#datos direccion cliente
            neworder.save()
            print('creado', neworder)
            orders = []
            for i in range(cantidad):
                if cantidad<100:
                    descuento = 0
                else:
                    descuento = 0.10

                neworderdetail = Orderdetails(last,producto.productid,producto.unitprice,cantidad,descuento)
                neworderdetail.save()
                orders.append(neworderdetail)
                
                print('creado', neworderdetail)
            #pedidoserializado = OrderSerializer(neworder, many=False)
            detallesSerializados=OrderdetailsSerializer(orders, many=True)
            return Response(detallesSerializados.data,status=status.HTTP_200_OK)
        

                
                #crear una order detail
        
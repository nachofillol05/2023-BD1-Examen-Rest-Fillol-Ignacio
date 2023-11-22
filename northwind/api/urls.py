#crea un url especifico para api

from django.urls import path
from . import views

urlpatterns = [
    path('Customers/', views.Customers_all, name='Customers'),
    path('Customers/<str:pk>', views.Customers_id, name='Customerbyid'),
    path('CustomerStartletter/', views.get_by_start_letter, name='Customersbystartingletter'),
    path('Suppliers/', views.suppliers, name='Suppliers'),
    path('Suppliers/<int:pk>', views.suppliers_id, name='Suppliersbyid'),
    path('Categories/', views.categories, name='Categories'),
    path('Categories/<int:pk>', views.categories_id, name='Categoriesbyid'),
    path('Employees/', views.employees, name='Employees'),
    path('Employees/<int:pk>', views.employees_id, name='Employeesbyid'),
    path('Orders/', views.orders, name='Orders'),
    path('Orders/<int:pk>', views.orders_id, name='Ordersbyid'),
    path('OrderDetails/', views.orderdetails, name='OrderDetails'),
    path('OrderDetails/<int:pk>', views.orderdetails_id, name='OrderDetailsbyid'),
    path('Products/', views.products, name='Products'),
    path('Products/<int:pk>', views.products_id, name='Productsbyid'),
    
]
"""path('CustomerDemographics/', views.customerdemographics_all, name='CustomerDemographics'),
    path('CustomerDemographics/<str:pk>', views.customerdemographics_id, name='CustomerDemographicsbyid'),
    
    path('Region/', views.region_all, name='Region'),
    path('Region/<str:pk>', views.region_id, name='Regionbyid'),
    
    path('Shippers/', views.shippers_all, name='Shippers'),
    path('Shippers/<str:pk>', views.shippers_id, name='Shippersbyid'),
    
    
    
    path('Territories/', views.territories_all, name='Territories'),
    path('Territories/<str:pk>', views.territories_id, name='Territoriesbyid'),
    
    path('EmployeeTerritories/', views.employeeterritories_all, name='EmployeeTerritories'),
    path('EmployeeTerritories/<str:pk>', views.employeeterritories_id, name='EmployeeTerritoriesbyid'),
    path('CustomerCustomerDemo/', views.customercustomerdemo_all, name='CustomerCustomerDemo'),
    path('CustomerCustomerDemo/<str:pk>', views.customercustomerdemo_id, name='CustomerCustomerDemobyid'),"""
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
    path('OrderDetails/<int:pk>/<int:pk2>', views.orderdetails_id, name='OrderDetailsbyid'),
    path('Products/', views.products, name='Products'),
    path('Products/<int:pk>', views.products_id, name='Productsbyid'),
    path('ejemplo1/',views.ejemplo1,name='ejemplo1')
    
]
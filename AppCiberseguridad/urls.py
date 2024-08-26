from AppCiberseguridad import views 
from django.urls import path

urlpatterns = [
   
    path('producto/', views.Producto, name='producto'), 
    path('cliente/',views.Cliente , name='cliente'),
    path('opiniones/',views.Opiniones, name='opiniones'), 
    path('inicio/',views.Inicio , name='inicio' ) ,
    path('app-form/', views.app_form, name='AppForm'),
    path('busquedaCliente/', views.busquedaCliente, name='BusquedaCliente') ,
    path('buscar/', views.buscar) , 
 ]
 
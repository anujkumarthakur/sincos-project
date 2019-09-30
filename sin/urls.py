from django.urls import path
from . import views

urlpatterns = [
        path('',views.index,name='index'),
        path('primeryproduct/',views.primeryproduct,name='primeryproduct'),
        path('seconderypickandplaceproduct/',views.seconderypickandplaceproduct,name='seconderypickandplaceproduct'),
        path('seconderyandoflineproduct/',views.seconderyandoflineproduct,name='seconderyandoflineproduct'),
        path('about/',views.about,name='about'),
        path('services/',views.services,name='services'),
        path('contact/',views.contact,name='contact'),
        path('productdetail/',views.productdetail,name='productdetails'),
        path('machine1',views.machine1,name='machine1'),
        path('machine2',views.machine2,name='machine2'),
        path('machine3',views.machine3,name='machine3'),
        path('machine4',views.machine4,name='machine4'),
        path('machine5',views.machine5,name='machine5'),
        path('machine6',views.machine6,name='machine6'),
        path('machine7',views.machine7,name='machine7'),
        path('machine8',views.machine8,name='machine8'),
        path('machine9',views.machine9,name='machine9'),
        path('machine10',views.machine10,name='machine10'),
        path('machine11',views.machine11,name='machine11'),
        path('machine12',views.machine12,name='machine12'),
        path('machine13',views.machine13,name='machine13')
        ]

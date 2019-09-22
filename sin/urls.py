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
        path('productdetail/',views.productdetail,name='productdetails')
        ]

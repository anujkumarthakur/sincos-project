from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def primeryproduct(request):
    return render(request,'primeryproduct.html')


def seconderypickandplaceproduct(request):
    return render(request,'pickandplacesystem.html')


def seconderyandoflineproduct(request):
    return render(request,'andoflinepackgingsystem.html')


def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')
#products links
def productdetail(request):
    return render(request,'productitemsdetails.html')

# Create your views here.

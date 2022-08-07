from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
# Create your views here.

def index(request):
    return render(request,'products/index.html',{'Prod':Products.objects.all()})
    return HttpResponse("Welcom to Products")
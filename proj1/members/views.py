from django.shortcuts import render
from django.http import HttpResponse
from .models import Members
# Create your views here.

def index(request):
    # print(Members.objects.all())
    return render(request,'members/index.html',{'Mem':Members.objects.all()})
    # return HttpResponse("Welcom to members",{Members.objects.all().values})

from django.shortcuts import render
from  testapp.models import datamodel


# Create your views here.

def dataview(request):
    data=datamodel.objects.all()
    return render(request,'index.html',{'data':data})

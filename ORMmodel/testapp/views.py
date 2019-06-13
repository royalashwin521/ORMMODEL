from django.shortcuts import render
from testapp.models import employee
from django.db.models.functions import Lower
# Create your views here.

def display(request):
    e1=employee.objects.all()
    dict={'e1':e1}
    return render(request,"testapp/list.html",dict)

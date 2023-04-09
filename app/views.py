from django.shortcuts import render

# Create your views here.
from app.models import *

from django.db.models.functions import Length

def Employe(request):
    EMP=EMPLOYE_TABLE.objects.all()
    #EMP=EMPLOYE_TABLE.objects.filter(ENAME='SMITH')
    #EMP=EMPLOYE_TABLE.objects.order_by('ENAME')
    #EMP=EMPLOYE_TABLE.objects.order_by('-ENAME')
    #EMP=EMPLOYE_TABLE.objects.order_by(Length('ENAME'))
    #EMP=EMPLOYE_TABLE.objects.order_by(Length('ENAME').desc)
    EMP=EMPLOYE_TABLE.objects.all()
    EMP=EMPLOYE_TABLE.objects.filter(HIREDATE__gt='1980-04-19')
    EMP=EMPLOYE_TABLE.objects.filter(HIREDATE__gte='1980-04-19')
    EMP=EMPLOYE_TABLE.objects.filter(HIREDATE__lt='1980-04-19')
    EMP=EMPLOYE_TABLE.objects.filter(HIREDATE__lte='1981-04-19')

    

    
    
    
    
    
    d={'EMP': EMP}
    return render(request,'Employe.html',d)

def Department(request):
    DEPT=DEPERTMENT_TABLE.objects.all()
    d={'DEPT':DEPT}
    return render(request,'Department.html',d)

from django.db import models

# Create your models here.

class DEPERTMENT_TABLE(models.Model):
    DEPTNO=models.IntegerField(primary_key=True)
    DNAME=models.CharField(max_length=100)
    LOCATION=models.CharField(max_length=100)
    def __str__(self):
        return self.DNAME
    
class EMPLOYE_TABLE(models.Model):
    DEPTNO=models.ForeignKey(DEPERTMENT_TABLE,on_delete=models.CASCADE)
    EMPNO=models.IntegerField( default=0,primary_key=True)
    ENAME=models.CharField(max_length=100,unique=True) 
    JOB=models.CharField(max_length=100)
    MGR=models.IntegerField()
    HIREDATE=models.DateField()
    SALARY=models.IntegerField()
    COMMISION=models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.ENAME
    


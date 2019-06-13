from django.db import models

class customManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('esalary')

class employee(models.Model):
    eno= models.IntegerField()
    ename= models.CharField(max_length=30)
    esalary = models.IntegerField()
    ecity= models.CharField(max_length=30)
    objects = customManager()

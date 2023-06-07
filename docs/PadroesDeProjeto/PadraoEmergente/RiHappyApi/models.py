from django.db import models

# Create your models here.

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=200)

class Products(models.Model):
    ProductId = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=200)
    ProductPrice = models.DecimalField(max_digits=7, decimal_places=2)
    Department = models.CharField(max_length=200)

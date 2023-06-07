from rest_framework import serializers
from RiHappyApi.models import Products, Departments

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('DepartmentId', 'DepartmentName')

class ProductSerializer(serializers.ModelSerializer):
    ProductPrice = serializers.DecimalField(max_digits=7, decimal_places=2)
    class Meta:
        model=Products
        fields=('ProductId', 'ProductName','ProductPrice','Department')
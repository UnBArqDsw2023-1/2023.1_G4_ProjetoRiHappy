from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from RiHappyApi.models import Products, Departments
from RiHappyApi.serializers import DepartmentSerializer, ProductSerializer

# Create your views here.

@csrf_exempt
def departmentViewSet(request,id=0):
    if request.method =='GET':
        department_name = request.GET.get('departmentName')
        if department_name:
                departments = Departments.objects.filter(DepartmentName=department_name)
                if not departments:
                    return JsonResponse({"error": "Departamento não existe"}, status=400)
                else:            
                    departments_serializer = DepartmentSerializer(departments, many=True)
                    return JsonResponse(departments_serializer.data, safe=False)
            
        else:
            departments = Departments.objects.all()
            departments_serializer = DepartmentSerializer(departments,many=True)
            return JsonResponse(departments_serializer.data, safe=False)

    elif request.method =='POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Departamento adicionado com sucesso",safe=False)
        return JsonResponse("Falha ao adicionar departamento",safe=False)
    
    elif request.method == 'PUT':
        department_data= JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=id)
        departments_serializer = DepartmentSerializer(department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Departamento atualizado com sucesso",safe=False)
        return JsonResponse("Falha ao atualizar departamento",safe=False)
    
    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Departamento deletado",safe=False)
    
@csrf_exempt
def productViewSet(request,id=0):
    if request.method =='GET':       
        products = Products.objects.all()
        products_serializer = ProductSerializer(products,many=True)
        return JsonResponse(products_serializer.data, safe=False)

    elif request.method =='POST':
        product_data = JSONParser().parse(request)
        products_serializer = ProductSerializer(data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Produto adicionado com sucesso",safe=False)
        return JsonResponse("Falha ao adicionar produto",safe=False)
    
    elif request.method == 'PUT':
        product_data= JSONParser().parse(request)
        product = Products.objects.get(ProductId=id)
        products_serializer = ProductSerializer(product, data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Produto atualizado com sucesso",safe=False)
        return JsonResponse("Falha ao atualizar produto",safe=False)
    
    elif request.method == 'DELETE':
        product = Products.objects.get(ProductId=id)
        product.delete()
        return JsonResponse("Produto deletado",safe=False)
    

    
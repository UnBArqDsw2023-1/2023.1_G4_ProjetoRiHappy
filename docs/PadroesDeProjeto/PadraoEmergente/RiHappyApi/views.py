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
    

    
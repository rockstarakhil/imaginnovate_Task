from asyncio import Task
from rest_framework.response import Response
from rest_framework.decorators import api_view
from employe.models import Employe
from . serializers import EmployeSerializer
from api import serializers

@api_view(['GET'])
def AllEmployeData(request):
    Emplopye_data = Employe.objects.all()
    #Employe_salary = 
   # print(sal)
    serializer = EmployeSerializer(Emplopye_data,many=True)
    return Response(serializer.data)  

@api_view(['POST'])
def addEmploye(request):
    serializer = EmployeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def EmployeDetail(request,pk):
    EmployeData = Employe.objects.get(Employee_ID=pk)
   # sal = EmployeData.Salary
   # if sal <25000:
    #    serializer.Salary = sal
    serializer =  EmployeSerializer(EmployeData,many=False)
    return Response(serializer.data)
@api_view(['POST'])
def EmployeDetailEdit(request,pk):
    Employe = Employe.objects.get(Employee_ID=pk)
    serializer = EmployeSerializer(instance=Task,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])

def EmployeDelete(request,pk):
    emp = Employe.objects.get(Employee_ID=pk)
    emp.delete()
    return "employe Deleted Sucessfully !!"






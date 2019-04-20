from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Student

def get_student(request):
    allStudents = Student.objects.all()
    jsonList = []
    for field in allStudents:
        jsonField = {
            "name": field.name,
            "age": field.age,
            "roll_number": field.roll_number
        }
        jsonList.append(jsonField)
    response = {
        "data": jsonList
        
    }
    return JsonResponse(response)

def delete_student(request):
    Student.objects.filter(name="Daniel").delete()
    return HttpResponse("student deleted successfully!")

def put_student(request):
    student = Student.objects.get(name="Julia")
    student.name = "Mario"
    student.save()
    return HttpResponse("student updated successfully!")

def post_student(request):
    student = Student.objects.create(name="Ernesto", age=10, roll_number="Empleado")
    return HttpResponse("student posted successfully!")
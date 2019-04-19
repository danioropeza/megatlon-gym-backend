from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Student

def home(request):
    student_data = Student.objects.all()
    response = {
        "data": "123"
    }
    return JsonResponse(response)
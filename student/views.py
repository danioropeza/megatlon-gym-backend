from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from .models import ( Student )
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .serializers import (
    StudentDetailSerializers,
    StudentCreateSerializers,
)

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializers

class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializers

class StudentDetailAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializers

class StudentUpdateAPIView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializers

class StudentDeleteAPIView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializers

def home(request):
    context = {
        'allstudents': Student.objects.all()
    }
    return render(request, 'home.html', context)

class StudentListView(ListView):
    model = Student
    template_name = 'home.html'  
    context_object_name = 'students'
    #ordering = ['-date_posted']

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'

class StudentCreateView(CreateView):
    model = Student
    template_name = 'student_form.html'
    fields = ['name', 'age', 'roll_number']

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student_form.html'
    fields = ['name', 'age', 'roll_number']

class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/'
    template_name = 'student_confirm_delete.html'

def about(request):
    return render(request, 'about.html', {'title': 'About'})


class StudentListAPIView2(APIView):
    def get(self, request, format=None):
        students = Student.objects.all()
        serializer = StudentDetailSerializers(students, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentDetailSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentAPIView2(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentDetailSerializers(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentDetailSerializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
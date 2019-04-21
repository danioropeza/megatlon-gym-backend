from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from .models import Student
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
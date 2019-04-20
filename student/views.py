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

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/'
    template_name = 'student_confirm_delete.html'

def about(request):
    return render(request, 'about.html', {'title': 'About'})

# class StudentView(View):
#     def get(self, request):
#         allStudents = Student.objects.all()
#         jsonList = []
#         for field in allStudents:
#             jsonField = {
#                 "name": field.name,
#                 "age": field.age,
#                 "roll_number": field.roll_number
#             }
#             jsonList.append(jsonField)
#         response = {
#             "data": jsonList
            
#         }
#         return JsonResponse(response)

#     def delete(self,request):
#         Student.objects.filter(name="Daniel").delete()
#         return HttpResponse("student deleted successfully!")

# def put_student(request):
#     student = Student.objects.get(name="Julia")
#     student.name = "Mario"
#     student.save()
#     return HttpResponse("student updated successfully!")

# def post_student(request):
#     student = Student.objects.create(name="Ernesto", age=10, roll_number="Empleado")
#     return HttpResponse("student posted successfully!")
# def get_html(request):
#     return render(request, 'index.html')
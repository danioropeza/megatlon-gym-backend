"""mongo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student import views
from student.views import (
    StudentListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StudentListView.as_view(), name='blog-home'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('student/new/', StudentCreateView.as_view(), name='student-create'),
    path('student/<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
    path('about/', views.about, name='blog-about'),
]

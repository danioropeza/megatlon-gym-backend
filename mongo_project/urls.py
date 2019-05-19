from django.contrib import admin
from django.urls import path
from student import views
from student.views import (
    StudentListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
    StudentCreateAPIView,
    StudentListAPIView,
    StudentDetailAPIView,
    StudentUpdateAPIView,
    StudentDeleteAPIView,
    StudentListAPIView2,
    StudentAPIView2,
)

from client.views import (
    ClientCreateAPI,
    ClientListAPI,
    ClientDetailAPI,
    ClientUpdateAPI,
    ClientDeleteAPI
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StudentListView.as_view(), name='blog-home'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('student/new/', StudentCreateView.as_view(), name='student-create'),
    path('student/<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
    path('about/', views.about, name='blog-about'),

    path('api/student/new', StudentCreateAPIView.as_view(), name='create'),
    path('api/students/', StudentListAPIView.as_view(), name='list'),
    path('api/student/<int:pk>/', StudentDetailAPIView.as_view(), name='detail'),
    path('api/student/<int:pk>/update/', StudentUpdateAPIView.as_view(), name='update'),
    path('api/student/<int:pk>/delete/', StudentDeleteAPIView.as_view(), name='delete'),

    path('api2/students/', StudentListAPIView2.as_view(), name='students-api2'),
    path('api2/student/<int:pk>/', StudentAPIView2.as_view(), name='student-detail-api2'),

    #Integracion clase Client

    path('api/client/new', ClientCreateAPI.as_view(), name='create-client'),
    path('api/clients/', ClientListAPI.as_view(), name='list-client'),
    path('api/client/<int:pk>/', ClientDetailAPI.as_view(), name='detail-client'),
    path('api/client/<int:pk>/update/', ClientUpdateAPI.as_view(), name='update-client'),
    path('api/client/<int:pk>/delete/', ClientDeleteAPI.as_view(), name='delete-client'),
]

from rest_framework.serializers import ModelSerializer
from .models import Student

class StudentDetailSerializers(ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'name',
            'age',
            'roll_number'
        ]

class StudentCreateSerializers(ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'name',
            'age',
            'roll_number'
        ]
        

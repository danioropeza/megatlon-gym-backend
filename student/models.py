from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
import json 

class Student(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    name = models.CharField(max_length=20, null=True)
    age = models.IntegerField(default=20, null=True)
    roll_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.pk})
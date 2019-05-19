from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
import json 

class Client(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    name = models.CharField(max_length=20, null=True)
    ci = models.CharField(max_length=20, null=True)
    phoneNumber = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name
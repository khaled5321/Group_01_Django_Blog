from django.db import models
from django.shortcuts import get_object_or_404
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=120,default="Films")


    def __str__(self):
        return self.name

    @classmethod
    def get_specific_object(cls,id):
        return get_object_or_404(cls,pk=id)
    

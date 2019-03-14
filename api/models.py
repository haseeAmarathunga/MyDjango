from django.db import models

class Student(models.Model):
    st_id = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=5)

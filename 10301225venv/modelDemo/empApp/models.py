
from django.db import models


class Employee(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    salary = models.FloatField()
    email = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
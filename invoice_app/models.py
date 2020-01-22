from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
	employee_id = models.TextField()
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
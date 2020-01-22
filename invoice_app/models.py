from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
	employee_id = models.TextField()
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Articles(models.Model):
	title = models.CharField(max_length = 150, verbose_name = "tytuł")
	content = models.TextField(verbose_name = "zawartość")
	published = models.DateTimeField (verbose_name = "data publikacji")

	def __unicode__(self):
		return self.title
		
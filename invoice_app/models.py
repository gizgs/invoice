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

class Invoice(models.Model):
	invoice_id = models.AutoField(primary_key = True)
	invoice_user_id = "user_id"
	invoice_date_of_issue = models.DateField()
	invoice_nr = models.CharField(max_length = 250)
	invoice_name = models.CharField(max_length = 250)
	invoice_netto = models.FloatField()
	invoice_vat = models.FloatField()
	invoice_brutto = models.FloatField(default = 100)
	invoice_place = "nazwa miejscowości"
	invoice_file = models.FileField()

	def __unicode__(self):
		return self.invoice_nr
		
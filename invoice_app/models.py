from django.db import models
from django.contrib.auth.models import User


Place_CHOICES = (
    ('Żagań', 'Żagań'),
    ('Krasiczyn', 'Krasiczyn'),
    ('Kielce', 'Kielce'),
    ('Żory', 'Żory'),
    ('Nie dotyczy', 'Nie dotyczy'),
)

class Invoice(models.Model):
	invoice_id = models.AutoField(primary_key = True)
	invoice_date_of_issue = models.DateField('Data wystawienia')
	invoice_nr = models.CharField("Numer faktur", max_length = 250)
	invoice_name = models.CharField("Nazwa faktury", max_length = 250)
	invoice_netto = models.FloatField("Kwota netto")
	invoice_vat = models.FloatField("Vat")
	invoice_brutto = models.FloatField("Kwota brutto", default = 100)
	invoice_place = models.CharField("Miejsce którego dotyczy", max_length=20, choices=Place_CHOICES, default='Nie dotyczy')
	#invoice_file = models.FileField("Plik faktury")

	def __unicode__(self):
		return self.invoice_nr
		
from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = ('invoice_date_of_issue', 'invoice_nr', 'invoice_name', 'invoice_netto', 'invoice_vat', 'invoice_brutto', 'invoice_place') #'invoice_file')

class LoginForm(forms.Form):
  	username = forms.CharField()
  	password = forms.CharField(widget=forms.PasswordInput)
  	
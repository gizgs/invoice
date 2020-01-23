from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = ('invoice_date_of_issue', 'invoice_name',)
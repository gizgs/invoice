from django.shortcuts import render
from django.utils import timezone
from .models import Articles, Invoice

# Create your views here.
def post_list(request):
	articles = Articles.objects.filter(published__lte=timezone.now()).order_by('published')
	return render(request, 'invoice_app/post_list.html', {'articles' : articles})

def invoice_list(request):
	invoice = Invoice.objects.order_by('invoice_nr')
	return render(request, 'invoice_app/post_list.html', {'invoice' : invoice})
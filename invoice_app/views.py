from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Articles, Invoice

# Create your views here.
def post_list(request):
	articles = Articles.objects.filter(published__lte=timezone.now()).order_by('published')
	return render(request, 'invoice_app/post_list.html', {'articles' : articles})

def invoice_list(request):
	invoice = Invoice.objects.order_by('invoice_nr')
	return render(request, 'invoice_app/post_list.html', {'invoice' : invoice})

def invoice_detail(request, pk):
	#Invoice.objects.get(pk=pk)
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'invoice_app/invoice_detail.html', {'invoice': invoice})
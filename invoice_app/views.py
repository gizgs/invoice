from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Articles
from .models import Invoice
from .forms import InvoiceForm
from django.shortcuts import redirect


# Create your views here.
def post_list(request):
	articles = Articles.objects.filter(published__lte=timezone.now()).order_by('published')
	return render(request, 'invoice_app/post_list.html', {'articles' : articles})

def invoice_list(request):
	invoice = Invoice.objects.order_by('invoice_nr')
	return render(request, 'invoice_app/post_list.html', {'invoice' : invoice})

def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'invoice_app/invoice_detail.html', {'invoice': invoice})


def invoice_new(request):
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.save()
            return redirect('invoice_detail', pk=invoice.pk)
    else:
        form = InvoiceForm()
    return render(request, 'invoice_app/invoice_edit.html', {'form': form})


def invoice_edit(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == "POST":
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.save()
            return redirect('invoice_detail', pk=invo.pk)
    else:
        form = InvoiceForm(instance=invoice)
    return render(request, 'invoice_app/invoice_edit.html', {'form': form})
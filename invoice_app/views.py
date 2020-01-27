from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Invoice
from .forms import InvoiceForm, LoginForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login




# Create your views here.

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

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'], password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Uwierzytelnienie zakończyło się sukcesem')
                else:
                    return HttpResponse('Konto jest zablokowane')
            else:
                return HttpResponse('Nieprawidłowe dane uwierzytelniające')
    else:
        form = LoginForm()
    return render(request, 'invoice_app/login.html', {'form': form})
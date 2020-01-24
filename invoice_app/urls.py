from django.urls import path
from . import views

urlpatterns = [
	path('', views.invoice_list, name='invoice_list'),
	path('invoice/<int:pk>/', views.invoice_detail, name='invoice_detail'),
	path('invoice/new/', views.invoice_new, name='invoice_new'),

    #path('/a', views.post_list, name='post_list'),

]
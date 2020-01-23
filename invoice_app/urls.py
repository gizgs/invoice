from django.urls import path
from . import views

urlpatterns = [
	path('', views.invoice_list, name='invoice_list'),
	path('invoice/<int:pk>/', views.invoice_detail, name='invoice_detail'),
    #path('/a', views.post_list, name='post_list'),

]
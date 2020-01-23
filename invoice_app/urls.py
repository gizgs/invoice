from django.urls import path
from . import views

urlpatterns = [
	path('', views.invoice_list, name='invoice_list'),
    #path('/a', views.post_list, name='post_list'),

]


from django.urls import path
from . import views

urlpatterns = [
	path('product/', views.water_product),
	path('aboutus/', views.aboutus),
	path('submit_order/', views.submit_order),
	path('order_list/', views.order_list),
]
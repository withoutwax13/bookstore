from django.urls import path

from .views import OrderPageView

urlpatterns = [
    path('', OrderPageView.as_view(), name = 'orders')
]
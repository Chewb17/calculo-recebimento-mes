from django.urls import path
from .views import CustomAuthToken, SaleListView, RegisterView

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='api_login'),
    path('sales/', SaleListView.as_view(), name='api_sales'),
    path('sales/<int:pk>/', SaleListView.as_view(), name='sale-detail'),
    path('register/', RegisterView.as_view(), name='api_register'),
]
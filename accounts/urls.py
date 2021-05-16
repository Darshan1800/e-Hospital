from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import *

app_name = "accounts"

urlpatterns = [
    path('hospital/register', RegisterHospitalView.as_view(), name='hospital-register'),
    
    path('bloodbank/register', RegisterBloodBankView.as_view(), name='bloodbank-register'),

    
    path('supplier/register', RegisterSupplierBankView.as_view(), name='supplier-register'),

    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
]

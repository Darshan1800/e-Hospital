from django.urls import path, include
from bloodbank.views import DashboardView
from .views import *

app_name = "bloodbank"

urlpatterns = [
    
    path('dashboard/', include([
        path('', DashboardView.as_view(), name='bloodbank-dashboard'),
        path('bloodlist', BloodListView, name='blood-list'),
        path('bloodrequest', createbloodrequest, name='blood-create'),
        path('blood/<int:pk>/',BloodUpdateView.as_view(), name='blood-edit'),


       
    ])),
 
]

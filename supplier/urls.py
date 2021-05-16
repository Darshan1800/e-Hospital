from django.urls import path, include
from supplier.views import DashboardView ,createoxyrequest ,OxygenListView,OxygenUpdateView

app_name = "supplier"

urlpatterns = [
    
    path('dashboard/', include([
        path('', DashboardView.as_view(), name='supplier-dashboard'),
        path('oxygencreate/',createoxyrequest,name='supplier-create'),
        path('oxygenlist/',OxygenListView,name='oxgyen-list'),
        path('oxygen/<int:pk>/',OxygenUpdateView.as_view(), name='oxygen-edit'),

    ])),
 
]

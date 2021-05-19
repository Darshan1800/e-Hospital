from django.urls import path, include

from .views import *

app_name = "hospital"

urlpatterns = [
   
    path('dashboard/', include([
        path('', DashboardView.as_view(), name='hospital-dashboard'),
       path('doctorcreate', createdoctor, name='doctor-create'),
       path('doctorlist', DoctorListView, name='doctor-list'),
       path('doctoredit/<int:pk>/',ItemUpdateView.as_view(), name='doctor-edit'),
        path('roomcreate', createrooms, name='room-create'),
        path('roomlist', RoomListView, name='room-list'),
        path('roomedit/<int:pk>/',RoomUpdateView.as_view(), name='room-edit'),

        path('oxygenrequest', createoxyrequest, name='oxygen-create'),
        path('oxygenlist', OxygenListView, name='oxygen-list'),
        path('oxygen/<int:pk>/',OxygenUpdateView.as_view(), name='oxygen-edit'),


        
        path('bloodrequest', createbloodrequest, name='blood-create'),
        path('bloodlist', BloodListView, name='blood-list'),
        path('blood/<int:pk>/',BloodUpdateView.as_view(), name='blood-edit'),


        
        
        path('paitentrequest', createpaitentrequest, name='paitent-create'),
        path('paitentlist', PaitentListView, name='paitent-list'),
        path('paitent/<int:pk>/',PaitentUpdateView.as_view(), name='paitent-edit'),



        path('ambulancecreate', createambulancerequest, name='ambulance-create'),
        path('ambulancelist', AmbulanceListView, name='ambulance-list'),
        path('ambulance/<int:pk>/',AmbulanceEditView.as_view(), name='ambulance-edit'),

    ])),
 
]

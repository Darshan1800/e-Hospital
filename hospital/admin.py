from django.contrib import admin

# Register your models here.
from .models import DoctorModel,RoomModel,OxygenOrderModel,BloodOrderModel,Ambulance
class DoctoreAdmin(admin.ModelAdmin):

    list_display = ('hospital','doctor_name','phone_number','status' )
    search_fields = ('hospital', 'doctor_name' )

class RoomAdmin(admin.ModelAdmin):

    list_display = ('roomhospital','room_no','no_beds','filled_beds','rem_beds','status' )
    search_fields = ('roomhospital',  )

class BloodAdmin(admin.ModelAdmin):

    list_display = ('bloodhospital','bloodtype','required','status', )
    search_fields = ('bloodhospital','bloodtype'  )



class OxygenAdmin(admin.ModelAdmin):

    list_display = ('oxygenhospital','required','status', )
    search_fields = ('oxygenhospital',  )



class AmbulanceAdmin(admin.ModelAdmin):

    list_display = ('ambhospital','ambtype','status','drivername' )
    search_fields = ('ambhospital', 'drivername' )


admin.site.register(RoomModel, RoomAdmin)
admin.site.register(DoctorModel, DoctoreAdmin)
admin.site.register(OxygenOrderModel, OxygenAdmin)
admin.site.register(BloodOrderModel, BloodAdmin)
admin.site.register(Ambulance, AmbulanceAdmin)
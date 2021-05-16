from django.contrib import admin
from supplier.models import OxygenOrderModel

# Register your models here.

class OxygenAdmin(admin.ModelAdmin):
    list_display= ['oxygensupplier','no_cylinder','message','status']
    serach_fields =['oxygensupplier','status']


admin.site.register(OxygenOrderModel,OxygenAdmin)
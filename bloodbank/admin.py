from django.contrib import admin

from .models import BloodOrderModel

# Register your models here.

class BloodAdmin(admin.ModelAdmin):

    list_display = ('blooduser','bloodtype','required','status', )
    search_fields = ('blooduser','bloodtype'  )

admin.site.register(BloodOrderModel, BloodAdmin)
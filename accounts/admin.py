from django.contrib import admin

# Register your models here.
from .models import User
class UserAdmin(admin.ModelAdmin):

    list_display = ('email', 'role', 'first_name','last_name','is_active','is_superuser')
    search_fields = ('email', 'first_name','last_name' )



admin.site.register(User, UserAdmin)
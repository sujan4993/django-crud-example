from django.contrib import admin
from .models import Customer
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    def full_name(obj):
        return obj
    full_name.short_description='Name'
    list_display = (full_name,'email','contact_no','status',)
    list_filter = ('created_at','status')
    search_fields = ('first_name','last_name')

# admin.site.register(Customer,CustomerAdmin)
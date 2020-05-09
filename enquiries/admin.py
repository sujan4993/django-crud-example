from django.contrib import admin
from .models import EnquiryType,EnquirySource,Enquiry

# Register your models here.

@admin.register(EnquiryType)
class EnquiryTypeAdmin(admin.ModelAdmin):
    list_display =('type_name','type_color')

@admin.register(EnquirySource)
class EnquirySourceAdmin(admin.ModelAdmin):
    list_display =('source_name','source_color')

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    def full_name(obj):
        return obj
    full_name.short_description='Name'
    list_display = (full_name,'email','contact_no','created_at','enquiry_source','enquiry_type',)
    list_filter = ('created_at',)
    search_fields = ('first_name','last_name')
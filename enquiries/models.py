from django.db import models

# Create your models here.

class EnquiryType(models.Model):
    class Meta:
        db_table = 'mst_enquiry_types'
    
    type_name = models.CharField(max_length=50)
    type_color = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.type_name

class EnquirySource(models.Model):
    class Meta:
        db_table = 'mst_enquiry_sources'
    
    source_name = models.CharField(max_length=50)
    source_color = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.source_name


class Enquiry(models.Model):
    class Meta:
        db_table='tbl_enquiries'
        verbose_name_plural='Enquiries'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    enquiry_type = models.ForeignKey(EnquiryType,on_delete=models.CASCADE)
    enquiry_source = models.ForeignKey(EnquirySource,on_delete=models.CASCADE)
    

    def __str__(self):
        return ('%s %s' %(self.first_name,self.last_name))

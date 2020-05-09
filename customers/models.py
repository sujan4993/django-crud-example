from django.db import models

class Customer(models.Model):
    class Meta:
        db_table ='tbl_customers'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return ('%s %s' %(self.first_name,self.last_name))

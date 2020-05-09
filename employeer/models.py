from django.db import models

class Employeer(models.Model):
    class Meta:
       db_table ='tbl_employeer'

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
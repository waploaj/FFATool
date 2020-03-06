from django.db import models
from Person.models import OsposPeople

# Create your models here.
class OsposSuppliers(OsposPeople):
    person = models.ForeignKey(OsposPeople, models.DO_NOTHING)
    company_name = models.CharField(max_length=255)
    agency_name = models.CharField(max_length=255)
    account_number = models.CharField(unique=True, max_length=255, blank=True, null=True)
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_suppliers'

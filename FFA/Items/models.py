from django.db import models

# Create your models here.

class OsposItems(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    supplier = models.ForeignKey('OsposSuppliers', models.DO_NOTHING, blank=True, null=True)
    item_number = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255)
    cost_price = models.DecimalField(max_digits=15, decimal_places=2)
    unit_price = models.DecimalField(max_digits=15, decimal_places=2)
    reorder_level = models.DecimalField(max_digits=15, decimal_places=3)
    receiving_quantity = models.DecimalField(max_digits=15, decimal_places=3)
    item_id = models.AutoField(primary_key=True)
    pic_filename = models.CharField(max_length=255, blank=True, null=True)
    allow_alt_description = models.IntegerField()
    is_serialized = models.IntegerField()
    stock_type = models.IntegerField()
    item_type = models.IntegerField()
    tax_category_id = models.IntegerField()
    deleted = models.IntegerField()
    custom1 = models.CharField(max_length=255, blank=True, null=True)
    custom2 = models.CharField(max_length=255, blank=True, null=True)
    custom3 = models.CharField(max_length=255, blank=True, null=True)
    custom4 = models.CharField(max_length=255, blank=True, null=True)
    custom5 = models.CharField(max_length=255, blank=True, null=True)
    custom6 = models.CharField(max_length=255, blank=True, null=True)
    custom7 = models.CharField(max_length=255, blank=True, null=True)
    custom8 = models.CharField(max_length=255, blank=True, null=True)
    custom9 = models.CharField(max_length=255, blank=True, null=True)
    custom10 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ospos_items'

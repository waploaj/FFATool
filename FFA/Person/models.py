from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.AutoField(blank=False, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    city  = models.CharField(max_length=255)
    gender = models.IntegerField()

    class Meta:
        managed = False
        db_table = "person"





from django.db import models
from Person.models import Person

# Create your models here.
class Employee(Person):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="+")
    username = models.CharField(unique=True, blank=False, null=False, max_length=255)
    password = models.CharField(max_length=255)
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = "employee"


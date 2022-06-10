from django.db import models
import uuid
#from django_prices.models import MoneyField as BaseMoneyField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Employe(models.Model):
    Employee_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    FirstName = models.CharField(max_length=300)
    LastName = models.CharField(max_length=300)
    Email = models.EmailField(max_length = 200)
    PhoneNumber = PhoneNumberField(null=False, blank=False, unique=True)
    DOJ = models.DateField()
    Salary = models.IntegerField()
    #Tax = models.IntegerField()

    
from django.db import models
from management.models import Room

# Create your models here.

class customer(models.Model):
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    contact_no = models.IntegerField()
    email = models.EmailField()

class CustomerRoom(models.Model):
    customer = models.ForeignKey(customer,on_delete = models.SET_NULL,null = True)
    room = models.ForeignKey(Room, on_delete = models.SET_NULL, null = True)

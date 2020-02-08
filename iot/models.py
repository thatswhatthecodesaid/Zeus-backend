from django.db import models
from main.models import *

class Ac(models.Model):
    ac_io = models.BooleanField()
    ac_city = models.CharField(max_length=100)
    ac_temp = models.CharField(max_length=100)



class Usage(models.Model):
    name = models.CharField(max_length=100)
    appliance = models.ForeignKey(Appliances, on_delete=models.CASCADE)
    start = models.CharField(max_length=100)
    stop = models.CharField(max_length=100) #auto_now=False, auto_now_add=False


class ioModel(models.Model):
    appliance = models.ForeignKey(Appliances, on_delete=models.CASCADE)
    a_io = models.BooleanField()


class Lockout(models.Model):
    appliance = models.ForeignKey(Appliances, on_delete=models.CASCADE)
    a_lockout = models.BooleanField()


class tubeLight(models.Model):
    a_name = models.ForeignKey(Appliances, on_delete=models.CASCADE)
    a_io = models.BooleanField()


    def __str__(self):
        return self.a_name

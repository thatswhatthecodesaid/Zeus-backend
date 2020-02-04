from django.db import models


class U(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    score = models.CharField(max_length=10, default=0)

    def __str__(self):
        return self.name


class Appliances(models.Model):
    a_name = models.CharField(max_length=100)
    a_rating = models.CharField(max_length=100)
    a_kwh = models.CharField(max_length=100)
    a_priority = models.CharField(max_length=100)
    a_control = models.BooleanField() #1 = User Control, 0 - Auto Control
    a_lockout = models.BooleanField() #1 = on when locked , 0 - off whne locked
    

    def __str__(self):
        return self.a_name


class RoomPlan(models.Model):
    floor_id = models.IntegerField()
    appliances = models.ManyToManyField(Appliances)

    def __str__(self):
        return self.floor_id




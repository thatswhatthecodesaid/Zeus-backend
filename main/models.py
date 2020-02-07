from django.db import models


class Room(models.Model):
    room = models.CharField(max_length=100)

    def __str__(self):
        return self.room

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
    a_io = models.BooleanField()
    a_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.a_name


class kwhUsage(models.Model):
    appliance = models.ForeignKey(Appliances, on_delete=models.CASCADE)
    start = models.CharField(max_length=50)
    stop = models.CharField(max_length=50)




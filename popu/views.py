from django.shortcuts import render
from main.models import *
from iot.models import *
from django.http import HttpResponse, JsonResponse


def Rooms(request):
    ls = Room.objects.all()
    x = []
    for i in ls:
        x.append(i.room)
    print(x)
    print(ls)
    return JsonResponse(x ,safe=False)


def appliancesRoom(request):
    ls = Appliances.objects.all()
    x = []
    y = {}
    for i in ls:
        x.append(i.a_name)
        y[i.a_name] = i.a_room_id
    return JsonResponse(y, safe=False)
    

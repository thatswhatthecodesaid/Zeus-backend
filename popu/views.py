from django.shortcuts import render
from main.models import *
from iot.models import *
from django.http import HttpResponse, JsonResponse
import json
from main.serializers import *
from django.core import serializers

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
    z = []
    for i in ls:
        x.append(i.a_name)
        y[i.a_name, i.a_io] = (i.a_room_id)
    y = json.dumps(y)
    y = json.loads(y)
    print(y)
    return JsonResponse(y, safe=False)


def ApplianceAPI(request):
    appliance_json = serializers.serialize("json", Appliances.objects.all())
    data = {"appliance_json": appliance_json}
    struct = json.loads(appliance_json)
    return JsonResponse(struct, safe=False)
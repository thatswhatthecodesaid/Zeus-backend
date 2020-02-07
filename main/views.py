from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from .forms import *
from .serializers import *
from rest_framework import viewsets, permissions
from .v2 import *
from iot.algo import *
from django.http import HttpResponse


def Uview(request):
    if request.method == "POST":
        form = Uform(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            email = form.cleaned_data["email"]
            address = form.cleaned_data["address"]


            x = U(name=name, phone=phone)
            x.save()

            return JsonResponse("{'saved'}", safe=False)
    else:
        form = Uform()
    return JsonResponse("{'login'}", safe=False)


class USView(viewsets.ModelViewSet):
    queryset = U.objects.all()
    serializer_class = USerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly)


def ScoreUpdate(request,id):
    ls = U.objects.get(id=id)
    if request.method == "POST":
        form = Change_data(request.POST)
        if form.is_valid():
            score = form.cleaned_data['score']
            ls.score = score
            ls.save()
            return JsonResponse("{'Changed'}", safe=False)
    else:
        form = Change_data()
    return JsonResponse("{'Change_info'}", safe=False)


def a_view(request):
    if request.method == "POST":
        form = AppliancesForm(request.POST)
        if form.is_valid():
            a_name = form.cleaned_data['a_name']
            a_rating = form.cleaned_data['a_rating']
            a_kwh = form.cleaned_data['a_kwh']
            a_priority = form.cleaned_data['a_priority']
            a_control = form.cleaned_data['a_control']
            a_lockout = form.cleaned_data['a_lockout']
            a_io = form.cleaned_data['a_io']
            u = Appliances(
                a_name=a_name,
                a_rating=a_rating,
                a_kwh=a_kwh,
                a_priority=a_priority,
                a_control=a_control,
                a_lockout=a_lockout,
                a_io=a_io,
            )
            ap_info = {
                'a_name': a_name,
                'a_rating': a_rating,
                'a_kwh': a_kwh,
                'a_priority': a_priority,
                'a_control': a_control,
                'a_lockout': a_lockout,
                'a_io' : a_io
            }
            ap_info = json.dumps(ap_info)
            ap_info = json.loads(ap_info)
            u.save()
            print("appliances saved")
            return JsonResponse(ap_info, safe=False)

            
    else:
        form = AppliancesForm()
    
    return render(request, "main/app.html", {
        'form':form
    })


def kwhView(request):
    if request.method == "POST":
        form = BillForm(request.POST)
        if form.is_valid():
            appliance = form.cleaned_data['appliance']
            start = form.cleaned_data['start']
            stop = form.cleaned_data['stop']
            ls = Appliances.objects.get(a_name=appliance)
            print(priceCalcuation(ls.a_kwh, stop, start, ls.a_name))
            return HttpResponse(priceCalcuation(ls.a_kwh, stop, start, ls.a_name))
    else:
        form = BillForm()
    return render(request, "main/bill.html", {
        "form" : form
    })


def RoomView(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.cleaned_data["room"]
            x = Room(room=room).save()
    else:
        form = RoomForm()
    return render(request, "main/room.html", {
        "form" : form,
    })
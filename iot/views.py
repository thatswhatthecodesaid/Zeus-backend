from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .forms import *
from django.core.files.storage import FileSystemStorage
from main.v2 import *
from datetime import datetime, timedelta
from .algo import *
import time



def home(request):
    return render(request, "iot/home.html")


def acview(request):
    if request.method == "POST":
        form = AcIot(request.POST)
        if form.is_valid():
            a_name = form.cleaned_data["a_name"]
            ac_io = form.cleaned_data["ac_io"]
            ac_temp = form.cleaned_data['ac_temp']
            ls = Appliances.objects.get(a_name=a_name)
            print(ls.a_name)
            ls.ac_temp = float(ac_temp)
            ls.ac_io = ac_io
            ls.save()
    else:
        form = AcIot()
    return render(request, 'iot/acio.html', {
        'form' : form
    })



def Tempc(request):
    if request.method == "POST":
        form = AcForm(request.POST)
        print(request.method)
        if form.is_valid():
            a_name = form.cleaned_data["a_name"]
            ac_io = form.cleaned_data['ac_io']
            ac_temp = form.cleaned_data['ac_temp']
            ac_city = form.cleaned_data['ac_city']
            x = Ac(ac_io=ac_io, ac_temp=ac_temp, ac_city=ac_city)
            x.save()
            ac_temp = float(ac_temp)
            print(f'''
            bool = {ac_io}
            temp = {ac_temp}
            city = {ac_city}
            Data collected
            ''')
    else:
        form = AcForm()
    return render(request, "iot/temp.html", {
        "form" : form
    })


def ac_task(request):
    ls = Ac.objects.get(id=7)
    ls.ac_temp = float(ls.ac_temp) + 273
    task = Tempc2(ls.ac_city, ls.ac_io, ls.ac_temp)
    ap = {
                'ac_temp': ls.ac_temp,
                'city' : ls.ac_city,
                'ac_state' : ls.ac_io,
                'task': task,
                'ac_name':ls.a_name,
            }
    ap = json.dumps(ap)
    ap = json.loads(ap)
    return JsonResponse(ap, safe=False)


def usageView(request):
    if request.method == "POST":
        form = UsageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            appliance = form.cleaned_data['appliance']
            start = form.cleaned_data['start']
            stop = form.cleaned_data['stop']
            ls = Appliances.objects.get(a_name=appliance)
            applianceSimulator(ls.a_name, ls.a_kwh, stop, start, ls.a_name)
            x = Usage(appliance=appliance, start=start, stop=stop, name=name)
            x.save()
    else:
        form = UsageForm()
    return render(request, "iot/us.html", {
        "form" : form
    })


def lockout(request):
    if request.method == "POST":
        form = ioForm(request.POST)
        if form.is_valid():
            io = form.cleaned_data['io']
            ls = Appliances.objects.get(a_lockout=io)
            return HttpResponse(ls)
    else:
        form = ioForm()
    
    return render(request, "iot/io.html", {"form":form})


def applianceIo(request):
    if request.method == "POST":
        form = ioForm2(request.POST)
        print(request.POST)
        if form.is_valid():
            appliance = form.cleaned_data["appliance"]
            a_io = form.cleaned_data["a_io"]
            ls = Appliances.objects.get(a_name=appliance)
            ls.a_io = a_io
            ls.save()
    else:
        form = ioForm2()
    return JsonResponse("{'io'}", safe=False)


def changeLockout(request):
    if request.method == "POST":
        form = changeLockoutForm(request.POST)
        if form.is_valid():
            appliance = form.cleaned_data["appliance"]
            a_lockout = form.cleaned_data["a_lockout"]
            ls = Appliances.objects.get(a_name=appliance)
            ls.a_lockout = a_lockout
            ls.save()
            return HttpResponse(ls)
    else:
        form = changeLockoutForm()
    return render(request, "iot/lockout.html", {
        "form": form
    })



def tubelightView(request):
    if request.method == "POST":
        form = tubeLightForm(request.POST)
        if form.is_valid():
            a_name = form.cleaned_data["a_name"]
            a_lux = form.cleaned_data["a_lux"]
            a_io = form.cleaned_data["a_io"]
            x = tubeLight(a_name=a_name, a_io=a_io)
            ls = Appliances.objects.get(a_name=a_name)
            lux_sun = 10752
            a_lux = float(a_lux)
            if a_lux < lux_sun:
                ls.a_io = True
            elif a_lux > lux_sun:
                ls.a_io
            x.save()
    else:
        form = tubeLightForm()
    return render(request, "iot/lux.html", {
        "form" : form,
    })
            
from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('home/', csrf_exempt(views.home)),
    path("acview/", csrf_exempt(views.Tempc)),
    path("aciot/", csrf_exempt(views.acview)),
    path("ac/", csrf_exempt(views.ac_task)),
    path("usage/", csrf_exempt(views.usageView)),
    path("io/", csrf_exempt(views.lockout))


]
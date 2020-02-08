from django.urls import path, include
from .views import *


urlpatterns = [
    path("rooms/", Rooms),
    path("air/", appliancesRoom)
]
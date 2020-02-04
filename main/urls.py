from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usview', views.USView)


urlpatterns = [
    path("", csrf_exempt(views.Uview)),
    path('api/', include(router.urls)),
    path('api/change/<int:id>', csrf_exempt(views.ScoreUpdate)),
    path('api/appliances/', csrf_exempt(views.a_view)),
]
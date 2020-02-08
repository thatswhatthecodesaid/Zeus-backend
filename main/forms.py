from django import forms
from .models import *

class Uform(forms.ModelForm):
    class Meta:
        model = U
        fields = (
            'name',
            'phone',
            'email',
            'address',
        )


class Change_data(forms.ModelForm):
    class Meta:
        model = U
        fields = ("score",)


class AppliancesForm(forms.ModelForm):
    class Meta:
        model = Appliances
        fields = "__all__"


class BillForm(forms.ModelForm):
    class Meta:
        model = kwhUsage
        fields = "__all__"


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = "__all__"


class MLform(forms.Form):
    da = forms.CharField(max_length=100)   

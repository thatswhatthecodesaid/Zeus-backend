from django import forms
from .models import *
from main.models import *

class AcForm(forms.ModelForm):
    class Meta:
        model = Ac
        fields = "__all__"


class UsageForm(forms.ModelForm):
    class Meta:
        model = Usage
        fields = "__all__"


class ioForm(forms.Form):
    io = forms.BooleanField(required=False)


class ioForm2(forms.Form):
    a_io = forms.BooleanField(required=False)
    appliance = forms.CharField(max_length=100)


class changeLockoutForm(forms.ModelForm):
    a_lockout = forms.BooleanField(required=False)
    class Meta:
        model = Lockout
        fields = "__all__"


class luxForm(forms.Form):
    lux = forms.CharField(max_length=100)


class AcIot(forms.Form):
    CHOICES = (
        ("ac1", "Ac room"),
        ("ac2", "Ac bedroom")
    )
    a_name = forms.ChoiceField(choices=CHOICES)
    ac_io = forms.BooleanField(required=False)
    ac_temp = forms.CharField(max_length=100)


class tubeLightForm(forms.ModelForm):
    CHOICES = (
        ("tl1", "Tl Hall"),
        ("tl2", "Tl bedroom"),
        ("t13", "Tl Kitchen"),
    )
    a_name = forms.ChoiceField(choices=CHOICES)
    a_lux = forms.CharField(max_length=100)
    class Meta:
        model = tubeLight
        fields = "__all__"

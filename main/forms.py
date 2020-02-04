from django import forms
from .models import *

class Uform(forms.ModelForm):
    class Meta:
        model = U
        fields = "__all__"


class Change_data(forms.ModelForm):
    class Meta:
        model = U
        fields = ("score",)


class AppliancesForm(forms.ModelForm):
    class Meta:
        model = Appliances
        fields = "__all__"
        
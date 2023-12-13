from django import forms
from .models import Dealership, Lienholder

class DealershipForm(forms.ModelForm):
    class Meta:
        model = Dealership
        fields = "__all__"

class LienholderForm(forms.ModelForm):
    class Meta:
        model = Lienholder
        fields = '__all__'
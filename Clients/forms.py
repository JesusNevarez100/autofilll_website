from django.forms import ModelForm
from .models import Client

#Create form Fields
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"

        
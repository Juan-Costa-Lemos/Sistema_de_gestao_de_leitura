from dataclasses import field
from django.forms import ModelForm
from .models import Leituras

class LeituraForm(ModelForm):
    class Meta:
        model = Leituras
        fields = '__all__'
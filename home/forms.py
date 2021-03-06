from django.forms import ModelForm
from .models import Info
class Enterdata(ModelForm):
    class Meta:
        model = Info
        fields = ['full_name','tel','products','summ','lifetime']
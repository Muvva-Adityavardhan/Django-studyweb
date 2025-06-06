from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' #Based on the attributes of the model in models.py file, all those values will be asked(editable values)
        
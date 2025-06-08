from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' #Based on the attributes of the model in models.py file, all those values will be asked(editable values)
        exclude = ['host', 'participants'] #These values will not be asked in the form, as they are not editable by the user
        # exclude = ['host'] #This will not ask the host value, as it is not editable by the user
#These will be the classes that will be used to serialize the data(python object) for the API


from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'  # This will include all fields in the Room model
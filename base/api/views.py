from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer


@api_view(['GET'])
def getRoute(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]
    return Response(routes)
# This function returns a JSON response containing a list of API routes.
# The 'safe=False' argument allows the response to be a list instead of a dictionary.


@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True) #many means multiple objects or only one object
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request,pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False) #many means multiple objects or only one object
    return Response(serializer.data)
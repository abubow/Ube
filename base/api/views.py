# from django.http import JsonResponse

# def getRoutes(requests):
#     routes = [
#         'Get /api/',
#         'GET /api/rooms',
#         'GET /api/rooms/<str:pk>',
#     ]

#     return JsonResponse(routes, safe=False)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from base.api.serializers import RoomSerializer
@api_view(['GET'])
def getRoutes(requests):
    routes = [
        'Get /api/',
        'GET /api/rooms',
        'GET /api/rooms/<str:pk>',
    ]

    return Response(routes)

@api_view(['GET'])
def getRooms(requests):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(requests, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)
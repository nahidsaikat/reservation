from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from rooms.models import Room
from rooms.serializers import RoomSerializer


class RoomViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing rooms.
    """

    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    # permission_classes = [IsAuthenticated]

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from room_reservations.models import RoomReservation
from room_reservations.serializers import RoomReservationSerializer


class RoomReservationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing room reservations.
    """

    serializer_class = RoomReservationSerializer
    queryset = RoomReservation.objects.all()
    # permission_classes = [IsAuthenticated]

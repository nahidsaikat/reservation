import logging

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters import rest_framework as filters

from room_reservations.filters import RoomReservationFilter
from room_reservations.models import RoomReservation
from room_reservations.serializers import RoomReservationSerializer


logger = logging.getLogger(__name__)


class RoomReservationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing room reservations.
    """

    serializer_class = RoomReservationSerializer
    queryset = RoomReservation.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RoomReservationFilter
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        logger.info('Cancelling room reservation')
        rr = self.get_object()
        rr.is_cancelled = True
        rr.save()
        logger.info(f'Cancelled room reservation for {rr.employee.get_full_name()}')
        return Response(data={"status": "success"}, status=status.HTTP_200_OK)

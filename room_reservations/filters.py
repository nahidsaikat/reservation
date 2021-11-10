import django_filters

from room_reservations.models import RoomReservation


class RoomReservationFilter(django_filters.FilterSet):
    # employee = django_filters.CharFilter()

    class Meta:
        model = RoomReservation
        fields = ['employee']

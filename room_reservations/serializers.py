from rest_framework import serializers

from room_reservations.models import RoomReservation


class RoomReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomReservation
        fields = "__all__"

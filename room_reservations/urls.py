from django.urls import include, path
from rest_framework.routers import DefaultRouter

from room_reservations import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"room_reservation", views.RoomReservationViewSet, basename="room_reservation")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]

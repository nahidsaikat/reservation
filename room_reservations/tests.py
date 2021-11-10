# from django.test import TestCase
import json
from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from employees.factory import EmployeeFactory
from room_reservations.factory import RoomReservationFactory
from room_reservations.models import RoomReservation


class RoomReservationTest(APITestCase):
    def setUp(self):
        self.employee = EmployeeFactory()
        self.valid_payload = {
            "title": "Title 1",
            "from_date": str(datetime.now().date()),
            "to_date": str(datetime.now().date()),
            "employee": self.employee.id
        }
        self.invalid_payload = {
            "from_date": str(datetime.now().date()),
            "to_date": str(datetime.now().date()),
            "employee": self.employee.id
        }

    def test_create_room_reservation(self):
        response = self.client.post(
            reverse("room_reservation:room_reservation-list"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("title"), self.valid_payload.get("title"))

    def test_create_room_reservation_without_email_400(self):
        response = self.client.post(
            reverse("room_reservation:room_reservation-list"),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_room_reservation(self):
        rr = RoomReservationFactory()
        data = {"title": "title 2"}
        response = self.client.patch(
            reverse("room_reservation:room_reservation-detail", args=[rr.id]),
            data=json.dumps(data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("title"), data.get("title"))

    def test_room_reservation_details(self):
        rr = RoomReservationFactory()
        response = self.client.get(
            reverse("room_reservation:room_reservation-detail", args=[rr.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("id"), rr.id)
        self.assertEqual(response.data.get("title"), rr.title)

    def test_delete_room_reservation(self):
        rr = RoomReservationFactory()
        room_reservation_count = RoomReservation.objects.count()
        self.assertEqual(room_reservation_count, 1)
        response = self.client.delete(
            reverse("room_reservation:room_reservation-detail", args=[rr.id])
        )
        room_reservation_count = RoomReservation.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(room_reservation_count, 0)

    def test_cancel_room_reservation(self):
        rr = RoomReservationFactory()
        response = self.client.post(
            reverse("room_reservation:room_reservation-cancel", args=[rr.id])
        )
        db_rr = RoomReservation.objects.get(id=rr.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(db_rr.is_cancelled)

    def test_filter_by_employee_room_reservation(self):
        rr1 = RoomReservationFactory()
        rr2 = RoomReservationFactory()
        response = self.client.get(
            f'{reverse("room_reservation:room_reservation-list")}?employee={rr1.employee.id}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_room_reservation(self):
        rr1 = RoomReservationFactory()
        rr2 = RoomReservationFactory()
        response = self.client.get(
            f'{reverse("room_reservation:room_reservation-list")}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

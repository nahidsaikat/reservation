# from django.test import TestCase
import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from employees.models import Employee
from rooms.models import Room


class RoomTest(APITestCase):
    def setUp(self):
        user = Employee.objects.create(email='user@example.com')
        self.client.force_authenticate(user=user)

        self.valid_payload = {"name": "Room 1"}
        self.invalid_payload = {}

    def test_create_room(self):
        response = self.client.post(
            reverse("room:room-list"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("name"), self.valid_payload.get("name"))

    def test_create_room_without_email_400(self):
        response = self.client.post(
            reverse("room:room-list"),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_room(self):
        data = {"name": "Room 2"}
        response1 = self.client.post(
            reverse("room:room-list"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        response = self.client.patch(
            reverse("room:room-detail", args=[response1.data.get("id")]),
            data=json.dumps(data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), data.get("name"))

    def test_room_details(self):
        response1 = self.client.post(
            reverse("room:room-list"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        response = self.client.get(
            reverse("room:room-detail", args=[response1.data.get("id")])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("id"), response1.data.get("id"))
        self.assertEqual(response.data.get("name"), response1.data.get("name"))

    def test_delete_room(self):
        response1 = self.client.post(
            reverse("room:room-list"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        room_count = Room.objects.count()
        self.assertEqual(room_count, 1)
        response = self.client.delete(
            reverse("room:room-detail", args=[response1.data.get("id")])
        )
        room_count = Room.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(room_count, 0)

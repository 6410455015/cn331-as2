from datetime import timedelta
from django.contrib.auth.models import User
from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse

# NOTE: ปรับให้ตรง model ของจริง
from rooms.models import Room, Booking  # ถ้าชื่อไม่ตรง ให้แก้ import นี้

class BookingPathsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="bob", password="Passw0rd!")
        # สร้างห้องที่ "เปิดให้จอง"
        self.room = Room.objects.create(name="R101", is_open=True, capacity=10)

    def _login(self):
        self.client.post(reverse("login"), {"username": "bob", "password": "Passw0rd!"})

    def test_booking_good_path_under_1_hour(self):
        self._login()
        start = timezone.now().replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
        end = start + timedelta(minutes=50)   # ไม่เกิน 1 ชม.
        payload = {"room_id": self.room.id, "start": start.isoformat(), "end": end.isoformat()}

        # เปลี่ยน url-name ให้ตรง action สร้าง booking เช่น 'booking_create'
        res = self.client.post(reverse("booking_create"), data=payload, follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(Booking.objects.filter(room=self.room, user=self.user).exists())

    def test_booking_bad_path_over_1_hour(self):
        self._login()
        start = timezone.now().replace(minute=0, second=0, microsecond=0) + timedelta(hours=2)
        end = start + timedelta(hours=2)  # เกิน 1 ชม. => ควร error
        payload = {"room_id": self.room.id, "start": start.isoformat(), "end": end.isoformat()}

        res = self.client.post(reverse("booking_create"), data=payload)
        # คาดหวัง 400/422 หรือแสดง error message; ปรับตามโปรเจกต์จริง
        self.assertNotEqual(res.status_code, 200)
        self.assertFalse(Booking.objects.filter(room=self.room, start_time=start).exists())

    def test_booking_bad_path_room_closed(self):
        self._login()
        self.room.is_open = False
        self.room.save()

        start = timezone.now() + timedelta(hours=3)
        end = start + timedelta(minutes=30)
        payload = {"room_id": self.room.id, "start": start.isoformat(), "end": end.isoformat()}

        res = self.client.post(reverse("booking_create"), data=payload)
        self.assertNotEqual(res.status_code, 200)

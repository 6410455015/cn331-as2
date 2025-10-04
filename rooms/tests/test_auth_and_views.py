from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase, Client

class AuthAndBasicViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = "alice"
        self.password = "StrongPass123"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_success(self):
        res = self.client.post(reverse("login"), {"username": self.username, "password": self.password})
        # เปลี่ยน redirect url-name ให้ตรงของโปรเจกต์ เช่น 'room_list'
        self.assertEqual(res.status_code, 302)

    def test_login_fail(self):
        res = self.client.post(reverse("login"), {"username": self.username, "password": "wrong"})
        self.assertNotEqual(res.status_code, 302)   # ควรไม่ผ่าน/ไม่ redirect เข้าระบบ

    def test_room_list_accessible(self):
        # ถ้าต้องล็อกอินก่อนให้ login ก่อน
        self.client.login(username=self.username, password=self.password)
        res = self.client.get(reverse("room_list"))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Room")  # แค่เช็คข้อความใน template คร่าว ๆ

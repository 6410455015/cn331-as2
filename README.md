# 🗓️ Assignment 2 [CN331] — Room Booking

## 👥 สมาชิกกลุ่ม
- กนกวรรณ คุ้มโชคชนะ 6410615014
- รัชพล เยี่ยมกระโทก 6410455015

## 🎭 บทบาท (Roles)
- **ผู้ใช้ทั่วไป (User)** — ดูห้องที่เปิดให้จอง • จองห้อง ≤ 1 ชั่วโมง/ครั้ง
- **ผู้ดูแล (Admin)** — เปิด/ปิดห้อง • ดูรายการจองของแต่ละห้อง • แก้ไขเวลา/ยกเลิกการจองแทนผู้ใช้

---

## ✨ ฟีเจอร์ที่พัฒนา

### 🙋‍♀️ สำหรับ User
- **🔐 Register / Login / Logout** — หากยังไม่มีบัญชีสามารถสมัครสมาชิกและเข้าสู่ระบบได้
- **📋 Room List (หน้าแรก)** — แสดงรายการห้องทั้งหมดที่เปิดให้จอง
- **🏷️ Room Detail** — ดูรายละเอียดห้องและรายการจองในวัน–เวลาใดบ้าง
- **🗓️ Booking** — เลือกห้องและช่วงเวลาเพื่อจอง (**ไม่เกิน 1 ชั่วโมง/ครั้ง**)
- **📁 My Bookings** — ดู/ยกเลิกการจองของตนเอง

### 🛠️ สำหรับ Admin
- **🔑 Login / Logout**
- **🏢 Manage Rooms** — เปิด/ปิดห้อง • ดูรายการจองของห้อง • **แก้ไขเวลา/ยกเลิก** การจองของผู้ใช้
- **🧰 Django Admin** — จัดการข้อมูลเชิงลึก (เพิ่มผู้ใช้/เพิ่มห้อง/แก้รายละเอียด)

---
## 🎥 Demo Video

[![Watch Demo – Google Drive](https://img.shields.io/badge/Watch%20Demo-Google%20Drive-4285F4?logo=google-drive&logoColor=white)](https://drive.google.com/file/d/1mbSrIfGb3TuS7DF-pn69KE0HgwFFPNm_/view?usp=sharing)

## 📌 System Flow (Miro)

[![Open Miro Board](https://img.shields.io/badge/Miro-Open%20Board-ffca00?logo=miro&logoColor=000)](https://miro.com/app/board/uXjVJIw_vis=/?share_link_id=174491524429)

- 🧭 บอร์ดอธิบาย Flow ของ **ผู้ใช้ทั่วไป (User)** และ **ผู้ดูแลระบบ (Admin)** ตั้งแต่ Register/Login → Room List → Booking → My Bookings → Manage Rooms

## Unit Tests & Coverage

Run locally:
```bash
coverage run manage.py test
coverage report -m

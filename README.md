# Smart Care 🏥

**Smart Care** is a healthcare-based system developed using **Django REST Framework**, designed to simplify patient and doctor interactions, appointment bookings, and emergency support. The system supports both online and offline appointment booking, email confirmation for user accounts, and real-time bed availability monitoring.

## 🌐 Live Demo

Check out the live version here: [Smart Care Live](https://smart-care-f1uu.onrender.com)

---

## ⚙️ Features

- 👨‍⚕️ **Doctor & Patient Roles**
  - Separate roles for doctors and patients.
  
- 📅 **Appointment Booking**
  - Patients can book appointments online or offline.
  
- 🚨 **Emergency Access**
  - Emergency services available for patients.
  
- 🛏️ **Bed Availability**
  - Patients can view current hospital bed availability.

- ✅ **Email Verification**
  - Users must register using a valid email.
  - A confirmation link is sent to their email.
  - Only after clicking the link, the account becomes active.

- 🔐 **Secure Authentication**
  - Login is allowed only after successful email verification.

---

## 🔧 Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: SQLite / PostgreSQL (as needed)
- **Email**: Django Email System for verification
- **Hosting**: Render

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/smart-care.git
cd smart-care

# ✅ Task Tracker API (Django + DRF + Celery + Redis)

A Django REST Framework-based API to manage tasks and automatically send email reminders before deadlines.

Perfect for trainees showcasing skills in:
- Python & Django
- RESTful APIs
- Background jobs (Celery)
- Redis
- Email integration (SMTP)
- Secure credential handling (.env)

---

## 🚀 Features

- Create, view, and delete tasks
- Automatically schedule an email reminder **10 minutes before** a task’s due date
- Uses Celery + Redis for background scheduling
- Email credentials securely managed with `.env`

---

## 🛠️ Technologies Used

- Python 3.x
- Django
- Django REST Framework
- Celery
- Redis
- PostgreSQL / SQLite (for local)
- SMTP (Gmail)
- `python-decouple` for env config
- Git + GitHub

---

## 📁 Project Structure

task_tracker/
├── tasks/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── serializers.py
│ └── tasks.py
├── task_tracker/
│ ├── settings.py
│ ├── urls.py
│ └── celery.py
├── .env
├── requirements.txt
├── README.md
└── manage.py

---
📫 Email Reminder
When a task is created with a due date, the system will schedule a background task to send an email reminder 10 minutes before the due date.

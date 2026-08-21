# Django Basics Practice 🚀

Welcome to my **Django Basics Practice** repository! This repository contains my hands-on practice projects while learning the fundamentals of Django, a powerful Python web framework.

---

## 📚 Topics Covered

- Django Installation & Virtual Environment Setup
- Creating Projects & Modular Apps Structure
- URL Routing & App Configuration
- Views (`views.py`) & HTTP/JSON Responses (`JsonResponse`)
- Django Models (`models.py`) & Field Types
- Foreign Keys & Model Relationships (`on_delete`, `related_name`)
- Schema Migrations (`makemigrations` & `migrate`)
- Django Shell (`python manage.py shell`) & ORM Queries
- Basic API Endpoints (`GET` requests for JSON output)

---

## 🛠️ Technologies Used

- Python
- Django
- SQLite (Default Database)
- Git & GitHub
- Django REST Framework (Upcoming)

---

## 📁 Projects in this Repository

1. **`first_project/`** - Initial setup and basic request-response flow with `HttpResponse`.
2. **`student_management/`** - Full backend data model for a Student Management System using Foreign Keys (`Department` & `Student` models) and a basic JSON API endpoint (`/api/students/`).

```text
django-basics-practice/
│
├── first_project/          # Practice Project 1
├── student_management/      # Practice Project 2 (Student Management System)
│   ├── student_management/
│   ├── students/
│   └── manage.py
├── .gitignore
└── README.md

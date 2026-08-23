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
- Custom Forms (`forms.py`) & HTML Rendering (`render`)
- Global & App-level Custom Templates Configuration (`settings.py`)
- Basic API Endpoints (`GET` and `POST` requests handling)

---

## 🛠️ Technologies Used

- Python
- Django
- HTML5 / CSS3
- SQLite (Default Database)
- Git & GitHub
- Django REST Framework (Upcoming)

---

## 📁 Projects in this Repository

1. **`first_project/`** - Initial setup and basic request-response flow with `HttpResponse`.
2. **`student_management/`** - Backend data model for a Student Management System using Foreign Keys (`Department` & `Student` models), custom `forms.py` handling, HTML templates rendering, and a basic JSON API endpoint (`/api/students/`).

```text
django-basics-practice/
│
├── first_project/          # Practice Project 1
├── student_management/     # Practice Project 2 (Student Management System)
│   ├── student_management/ # Core project configuration
│   ├── students/           # Main app (Models, Views, Forms, URLs)
│   ├── templates/          # Global HTML Templates (home.html)
│   └── manage.py
├── .gitignore
└── README.md

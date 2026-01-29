# Flipr Client Website

This is a full-stack Django web application built as part of a Flipr placement assignment.

## Features

### Landing Page
- Our Projects section (dynamic from database)
- Happy Clients section (dynamic from database)
- Contact form (stores data in backend)
- Newsletter subscription

### Admin Panel
- Manage projects (add image, name, description)
- Manage clients (add image, name, designation, description)
- View contact form responses
- View subscribed email addresses

### Bonus Feature
- Automatic image cropping to **450×350** on upload (admin side)

---

## 🛠 Tech Stack
- Backend: Django
- Database: SQLite
- Frontend: HTML, CSS
- Image Processing: Pillow

---

##  How to Run Locally

```bash
git clone <repo-url>
cd flipr-client-website
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

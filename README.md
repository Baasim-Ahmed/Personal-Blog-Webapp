# 📝 Django Blog App with Comments & Categories

A dynamic blog application built with Django that allows users to read categorized posts and leave comments. The project emphasizes clean UI with Bootstrap and intuitive content navigation.

## 🚀 Features

- 📚 Categorized blog posts
- 🗨️ User comments on individual blog posts
- 🧵 Detailed post view with timestamped comments
- 🎨 Responsive and modern UI with Bootstrap
- 🛠️ Django admin panel for managing posts and categories

## 🛠️ Tech Stack

- **Backend:** Django 5.x (Python)
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite3
- **Templating Engine:** Django Templates

## 📸 Screenshots

> Add screenshots here if available (e.g., post list page, post detail with comments, admin panel, etc.)

## 📂 Project Structure

blog_project/
├── blog/
│ ├── migrations/
│ ├── static/
│ ├── templates/
│ │ └── blog/
│ │ ├── base.html
│ │ ├── post_list.html
│ │ └── post_detail.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── blog_project/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── db.sqlite3
└── manage.py

## ⚙️ Setup Instructions

1. **Clone the repository**

git clone https://github.com/yourusername/blog-project.git
cd blog-project

2. **Create and activate a virtual environment**
python -m venv env
env\Scripts\activate  # On Windows
OR
source env/bin/activate  # On Unix/macOS

3. **Install dependencies**
pip install django

4. **Apply migrations**
python manage.py makemigrations
python manage.py migrate

5. **Create superuser (for admin access)**
python manage.py createsuperuser

6. **Run the server**
python manage.py runserver

🧑‍💻 Admin Panel
Access the admin dashboard at http://127.0.0.1:8000/admin using your superuser credentials to manage posts, categories, and comments.

📌 Future Enhancements
Add user authentication for posting comments

Like system for posts

Tag support in addition to categories

Pagination and search functionality

# 🛒 eCommerce Website

This is a full-stack eCommerce website built using Django (Python backend), SQL (database), Bootstrap, HTML, CSS, and JavaScript (frontend). The platform supports user registration, product listings, shopping cart functionality, order processing, and admin management.

---

## 🚀 Features

- User authentication (Login, Register, Logout)
- Product browsing with categories
- Shopping cart and checkout system
- Admin panel for product and order management
- Responsive design using Bootstrap
- Interactive frontend using JavaScript

---

## 🛠️ Tech Stack

| Category     | Technology              |
|--------------|--------------------------|
| Backend      | Python, Django           |
| Database     | SQLite / MySQL           |
| Frontend     | HTML, CSS, Bootstrap     |
| Scripting    | JavaScript               |
| Admin Panel  | Django Admin             |

---

## 📁 Folder Structure

ecommerce/
├── ecommerce/ # Main project folder
│ ├── settings.py # Project settings
│ ├── urls.py # URL routing
│ └── wsgi.py # WSGI entry point
├── store/ # Core app
│ ├── models.py # Database models
│ ├── views.py # Business logic
│ ├── urls.py # App-level routes
│ ├── templates/ # HTML templates
│ └── static/ # CSS, JS, images
├── manage.py # Django command-line tool
└── requirements.txt # Python dependencies

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ecommerce-django.git
cd ecommerce-django
2. Create a Virtual Environment
bash
Copy
Edit
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Configure the Database
By default, SQLite is used. To use MySQL:

Install MySQL server

Update DATABASES in ecommerce/settings.py with your MySQL credentials

python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecommerce_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
5. Run Migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
6. Create a Superuser
bash
Copy
Edit
python manage.py createsuperuser
7. Run the Development Server
bash
Copy
Edit
python manage.py runserver
Open your browser and go to: http://localhost:8000


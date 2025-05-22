# RetailIQ: Smart Inventory & Sales Analytics

A Django-powered dashboard for real-time retail stock monitoring and purchase insights. Features secure login and interactive visualizations to help retailers make smarter decisions.

---

## 📌 Problem Statement

Small retailers and vending businesses often rely on manual inventory tracking and inefficient purchase monitoring. This causes stockouts, lost sales, and lack of actionable insights.

---

## ✅ Solution

**RetailIQ** offers a **secure web dashboard** that:

- Monitors product stock levels in real-time  
- Visualizes sales and purchase data interactively  
- Protects admin access with hashed passwords  
- Provides data-driven insights for smarter business decisions  

---

## 🧰 Tech Stack

- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, JavaScript, Bootstrap  
- **Database:** SQLite (default), PostgreSQL, MySQL  
- **Authentication:** Django Admin with secure password hashing  

---

## 🚀 Features

- 🔐 Secure Admin Login  
- 📊 Interactive Purchase & Sales Dashboard  
- 📦 Product & Inventory Management  
- 💳 Order, Payment & Transaction Tracking  
- ⚙️ Multi-database support (SQLite, PostgreSQL, MySQL)  

---

## ⚡ Productivity Benefits

- Digitizes and centralizes inventory management  
- Provides real-time operational visibility  
- Enhances decision-making through visual analytics  
- Automates data collection, saving time and reducing errors  

---

## 🗂️ Project Structure
.
├── ## Structure
├── ```plaintext
├── project-root/
├── ├── manage.py                   # Django management script
├── ├── db.sqlite3                  # SQLite database file
├── ├── databaseApp/                # Main Django application
├── │   ├── __init__.py
├── │   ├── admin.py                # Admin site configuration
├── │   ├── apps.py                 # Application config
├── │   ├── machine_state.py        # Logic for machine state management
├── │   ├── models.py               # Database models
├── │   ├── tests.py                # App-specific tests
├── │   ├── urls.py                 # Application URLs
├── │   ├── utils.py                # Utility functions
├── │   ├── views.py                # View logic
├── │   ├── migrations/             # Database migration files
├── │   │   ├── __init__.py
├── │   │   ├── 0001_initial.py
├── │   │   ├── 0002_orderdetails_deleted_at.py
├── │   │   ├── 0003_product_productstock.py
├── │   │   ├── 0004_delete_product_alter_productstock_options.py
├── │   │   └── __pycache__/        # Compiled migration files
├── │   └── __pycache__/            # Compiled Python files for the app
├── ├── projectdatabase/            # Django project settings
├── │   ├── __init__.py
├── │   ├── asgi.py                 # ASGI application setup
├── │   ├── settings.py             # Project-wide settings
├── │   ├── urls.py                 # Project-level URL configuration
├── │   ├── wsgi.py                 # WSGI application setup
└── │   └── __pycache__/            # Compiled Python files


---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/retailiq.git
cd retailiq
```

````markdown
## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### 1️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

> 💡 You can generate this file with:
>
> ```bash
> pip freeze > requirements.txt
> ```

### 3️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ Create Superuser (for Admin Panel)

```bash
python manage.py createsuperuser
```

Follow the prompt to set a username and password.

### 5️⃣ Run the Development Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) to access the admin dashboard.

---

## 📸 Screenshots (Optional)

*Add screenshots of your dashboard, login page, or visual analytics here for recruiters.*

---

## 👨‍💻 Author

**Sai Krishna Chowdary Chundru**
🔗 [LinkedIn](https://www.linkedin.com/in/sai-krishna-chowdary-chundru)
🐙 [GitHub](https://github.com/sAI-2025)





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
├── databaseApp
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-311.pyc
│   │   ├── admin.cpython-311.pyc
│   │   ├── apps.cpython-311.pyc
│   │   ├── machine_state.cpython-311.pyc
│   │   ├── models.cpython-311.pyc
│   │   ├── urls.cpython-311.pyc
│   │   ├── utils.cpython-311.pyc
│   │   └── views.cpython-311.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── machine_state.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_orderdetails_deleted_at.py
│   │   ├── 0003_product_productstock.py
│   │   ├── 0004_delete_product_alter_productstock_options.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-311.pyc
│   │       ├── 0002_orderdetails_deleted_at.cpython-311.pyc
│   │       ├── 0003_product_productstock.cpython-311.pyc
│   │       ├── 0004_delete_product_alter_productstock_options.cpython-311.pyc
│   │       └── __init__.cpython-311.pyc
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── projectdatabase
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-311.pyc
    │   ├── settings.cpython-311.pyc
    │   ├── urls.cpython-311.pyc
    │   └── wsgi.cpython-311.pyc
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/retailiq.git
cd retailiq


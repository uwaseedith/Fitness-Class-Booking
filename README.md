# 🏋️‍♀️ Fitness Class Booking System

A full-stack Django-based web application that allows users to register, view class schedules, book fitness sessions, and receive email notifications. Built with PostgreSQL, Docker, MailHog, Nginx, and deployed via Ansible.

---

## 🚀 Features

- ✅ User registration and login
- 📅 Browse and search fitness classes
- 🧾 Book sessions and receive confirmation emails
- 📬 Email notification system (SendGrid or MailHog)
- 📦 PostgreSQL database
- 🐳 Fully Dockerized (Django, PostgreSQL, Nginx, MailHog)
- 🤖 CI/CD ready (GitHub Actions + Docker Hub)
- 📡 Remote deployment using Ansible

---

## 📁 Project Structure

```
Fitness-Class-Booking/
│
├── bookings/                # Django app
├── config/                  # Django project settings
├── templates/               # HTML templates
├── staticfiles/             # Collected static files
├── Dockerfile               # Dockerfile for Django + Gunicorn
├── docker-compose.yml       # Orchestrates Docker services
├── requirements.txt         # Python dependencies
├── ansible/
│   ├── hosts                # Ansible inventory
│   └── playbook.yml         # Ansible deployment steps
└── README.md
```

---

## ⚙️ Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Fitness-Class-Booking.git
cd Fitness-Class-Booking
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run Locally with SQLite (for quick testing)

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🐳 Running with Docker

### 1. Build and Run Containers

```bash
docker-compose up --build
```

- App: [http://localhost](http://localhost)
- MailHog: [http://localhost:8025](http://localhost:8025)

### 2. Apply Migrations + Create Superuser

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

---

## 📬 Email Configuration

In `.env` or environment variables:

```
EMAIL_HOST_USER=youremail@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

Or use MailHog (default in Docker: `EMAIL_HOST=mailhog`, `EMAIL_PORT=1025`)

---

## 🤖 Ansible Deployment

### 1. Prepare the Server

- Provision a remote server (Ubuntu)
- Ensure Docker & Ansible are installed
- Make sure your SSH public key is added to the server's `~/.ssh/authorized_keys`

### 2. Update the Inventory File

Edit `ansible/hosts`:

```ini
[fitness_app]
64.23.210.235 ansible_user=pelin ansible_ssh_private_key_file=~/.ssh/id_rsa ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

### 3. Run Deployment

```bash
ansible-playbook -i ansible/hosts ansible/playbook.yml
```

The playbook will:

- Ensure Docker is installed
- Pull the latest Docker image
- Run the app with `docker-compose up -d`

---

## 🧪 Testing

- Test login/signup
- Try booking a class and check for email
- View emails at [http://localhost:8025](http://localhost:8025) when using MailHog

---

## 🧠 Credits

Developed by Ardine 🚀  
Backend: Django • DB: PostgreSQL • CI/CD: Ansible + Docker

---

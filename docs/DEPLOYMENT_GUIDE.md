# Netriva Collection Deployment Guide

## Development Environment

### Requirements

* Python 3.14+
* Node.js 22+
* PostgreSQL
* Git
* VS Code

---

## Backend Setup

Create Virtual Environment

python -m venv venv

Activate

venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Run Server

python manage.py runserver

---

## Frontend Setup

Install Packages

npm install

Run Development Server

npm run dev

---

## Production Setup

### Backend

Platform:
Render

Environment Variables

SECRET_KEY=

DEBUG=False

DATABASE_URL=

CLOUDINARY_URL=

ALLOWED_HOSTS=

---

### Frontend

Platform:
Vercel

Environment Variables

NEXT_PUBLIC_API_URL=

---

## Database

Production Database

PostgreSQL

Migration Commands

python manage.py makemigrations

python manage.py migrate

---

## Static Files

python manage.py collectstatic

---

## Deployment Checklist

* Environment Variables Configured
* PostgreSQL Connected
* Cloudinary Connected
* Migrations Applied
* Static Files Collected
* Domain Connected
* SSL Enabled

Deployment Status:
Not Started

# FLASK_Webpage
A Flask-based personal blog and portfolio website with CRUD posts, project showcase, and a contact page. Built with Flask, SQLAlchemy, and Jinja2 templates.
# Flask Blog & Portfolio Website

This repository contains a **Flask-based Blog + Portfolio web application**, built to showcase personal projects, write blog posts, and provide an easy way for visitors to get in touch.  
It includes a full CRUD blogging system, static portfolio pages, and a simple contact form.

---

## 🚀 Features

### 📝 Blog System (CRUD)
- Create, read, update, and delete blog posts  
- Stores posts using **SQLite + SQLAlchemy ORM**  
- Posts ordered by most recent  
- Flash messages for user feedback (success/error)

### 💼 Portfolio Pages
- `/about` – Personal summary  
- `/projects` – Predefined list of projects with title, description, and tags  
- Fully customizable Jinja templates

### 📬 Contact Page
- Simple contact form  
- Validates name/email/message  
- Uses Flask `flash()` to notify success or missing fields  

### 🧱 Tech Stack
- **Python, Flask**
- **SQLite** (default DB)
- **SQLAlchemy ORM**
- **Jinja2 Templates**
- HTML / CSS / Bootstrap (optional depending on your templates)

---

## 📁 Project Structure


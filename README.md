📚 Online Course Management System (OCMS)

This project is a full-stack Online Course Management System built as a capstone project.

The goal was to design and implement a secure, scalable backend using Django and PostgreSQL, while also building a functional frontend using pure HTML, CSS, and JavaScript — without relying on frontend frameworks.

The system supports different user roles and demonstrates real-world backend concepts like JWT authentication, role-based access control, caching with Redis, filtering, pagination, and relational database design.

🚀 What This Project Does

The platform allows:

Users to log in using JWT authentication

Students to browse, filter, search, and enroll in courses

Instructors to create and manage courses

Admins to manage categories and monitor platform statistics

Dashboard data to be cached using Redis for performance

It is designed to simulate how a real learning management system (LMS) backend would work.

👥 User Roles
👑 Admin

Create course categories

View system statistics (cached via Redis)

👨‍🏫 Instructor

Create courses

Set course level and price

👨‍🎓 Student

Browse courses

Filter by level

Search by title

Sort by price

Enroll in courses

Submit reviews

View enrolled courses

🧱 Tech Stack

Backend

Django

Django REST Framework

PostgreSQL

JWT (SimpleJWT)

Redis (for caching)

Frontend

HTML

CSS

JavaScript (Vanilla)

Other Tools

Hoppscotch / Postman (API testing)

Git & GitHub

🗄️ Database Design

The database is normalized and follows a structured relational schema.

Main components include:

Custom User model (with role field)

Categories

Courses

Modules

Lectures

Enrollments

Lecture Progress

Reviews

Key improvements:

Indexed fields for performance

Composite unique constraints (e.g., no duplicate enrollments)

Proper foreign key relationships

Optimized for PostgreSQL

🔐 Authentication & Security

JWT-based authentication

Role-based permissions on protected endpoints

Password hashing

Enrollment and review duplication prevention

Stateless authentication system

All sensitive APIs require a valid JWT token.

📊 Redis Caching

Redis is used for caching dashboard statistics like:

Total users

Total courses

Total enrollments

This reduces database load and demonstrates performance optimization techniques.

📡 API Endpoints Overview
Authentication
POST /api/token/
POST /api/token/refresh/
Courses
GET  /api/courses/courses/
POST /api/courses/courses/
GET  /api/courses/categories/
Enrollments
GET  /api/enroll/
POST /api/enroll/
Reviews
GET  /api/reviews/
POST /api/reviews/
Dashboard
GET /api/dashboard/
⚙️ How to Run This Project
1️⃣ Clone the repository
git clone https://github.com/argha0203/OCMS_Capstone_PEP.git
cd OCMS_Capstone_PEP
2️⃣ Create a virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install dependencies
pip install django djangorestframework psycopg2-binary
pip install djangorestframework-simplejwt
pip install django-redis django-filter django-cors-headers
4️⃣ Configure PostgreSQL

Create database:

CREATE DATABASE ocms_db;
CREATE USER ocms_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE ocms_db TO ocms_user;

Update database settings inside settings.py.

5️⃣ Apply migrations
python manage.py makemigrations
python manage.py migrate
6️⃣ Seed sample data

Use Django shell and run the provided seed script.

7️⃣ Start backend server
python manage.py runserver

Backend runs at:

http://127.0.0.1:8000
8️⃣ Run frontend

Open index.html

OR

python -m http.server 5500

Frontend:

http://localhost:5500
🔑 Demo Credentials
Admin
admin@gmail.com
1234
Instructor
instructor1@gmail.com
1234
Student
student@gmail.com
1234
🎯 Academic Requirements Covered

PostgreSQL as primary database

JWT authentication mandatory

Redis caching implemented

Pagination enabled

Filtering and ordering implemented

Frontend built using HTML/CSS/JS only

All required constraints have been implemented.

🧠 What This Project Demonstrates

Custom Django user model

Role-based API permissions

REST API design

PostgreSQL schema design

Redis caching integration

Full-stack integration

Clean modular Django structure

Production-style backend thinking

🚀 Possible Improvements

Payment gateway integration

Video upload & streaming

Deployment with Docker

Cloud hosting (AWS / Render)

Instructor analytics dashboard

Automated test suite

👨‍💻 About This Project

This project was built as part of a capstone requirement to demonstrate backend system design and full-stack integration skills.

The focus was not just on making it work, but on structuring it in a way that reflects real-world backend architecture principles.

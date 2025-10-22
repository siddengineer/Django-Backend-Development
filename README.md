# Django-Backend-Development
A collection of Django backend concepts and projects covering REST APIs, authentication, CRUD operations, and more — ideal for learning and real-world development.

# 🛠️ Django Backend Projects Collection

This repository contains a series of backend projects built using the Django framework and Django REST Framework (DRF). Each project demonstrates real-world backend features such as authentication, CRUD operations, API development, and deployment-ready configurations.

## 💡 Key Features

- 🔐 User authentication (JWT, session-based)
- 📦 RESTful APIs using Django REST Framework
- 🗃️ PostgreSQL / SQLite integration
- 🧱 Clean, modular architecture
- ⚙️ Dockerized setups (where applicable)
- 🧪 Test coverage in select projects
- 🌐 Ready for deployment (Heroku, Render, etc.)

## 📂 Projects Overview

The repo will include projects such as:

- ✅ User Authentication API
- ✅ Simple Blog Backend (CRUD + user system)
- ✅ Task Manager API with filtering and deadlines
- ✅ E-commerce Backend with cart & orders
- ✅ Notes/Journal App with tags and search
- ✅ Open API documentation using Swagger or ReDoc

> All projects are standalone, beginner-friendly, and follow Django best practices.

## 📦 Installation (Generic for all projects)

```bash
# Clone the repo
git clone https://github.com/siddengineer/Django-Backend-Development.git

# Navigate to a project directory
cd project-folder-name

# Set up virtual environment and install dependencies
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt

# Run migrations and start server
python manage.py migrate
python manage.py runserver

```
🧠 Ideal For

Beginners learning Django & APIs

Developers building their portfolio

Real-world API practice for job readiness

Anyone looking to understand backend architecture

🤝 Contributions

Feel free to fork the repo, suggest improvements, or submit your own Django projects via pull requests!

⭐ Star this repository to support the project and get updates!

django documentation:https://docs.djangoproject.com/en/5.2/

Important resources
|   Name                       |               Link                                    |
|--------------------------|---------------------------------------------------|
|Custom Middleware                          |https://youtu.be/ELOgWKQpxB8?si=jUKX3GiJ7Ltj8gGp                                                   |
|QuerySet Evaluation in Django                          |https://github.com/siddengineer/Django-Backend-Development/blob/main/QuerySet%20Evaluation%20in%20Django                                                   |
|F() Expressions in Django                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |



|   NAME                        |                                LINK                 |
|--------------------------|---------------------------------------------------|
|WHAT IS WEB FRAMEWORK                          |https://github.com/siddengineer/Django-Backend-Development/blob/main/what%20is%20web%20framework%3F%3F                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |
|                          |                                                   |



| No. |                      Idea                       |                            What You’ll Learn                             |                 Link                 |
|-----|--------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------|
|  1  |              Request Timer                       |        Measure how long a request takes (already done).                 |                                     |
|  2  |         Add Custom Header to Response            |        Learn to modify outgoing HTTP responses.                         |                                     |
|  3  |         Block Requests Based on IP               |        Practice accessing request metadata and blocking logic.          |                                     |
|  4  |         Maintenance Mode Middleware              |        Return a static "site under maintenance" response based on a flag.|                                     |
|  5  |         User Agent Logger                        |        Log or restrict access based on user-agent (e.g., block bots).   |                                     |
|  6  |         Enforce HTTPS                            |        Redirect HTTP to HTTPS manually (if not using security middleware).|                                   |
|  7  |         JWT Token Checker                        |        Parse Authorization header and validate token (basic mock).      |                                     |
|  8  |         Request Body Logger                      |        Log POST data (with caution — useful for debugging only).        |                                     |
|  9  |         Locale Detector                          |        Detect language preference via headers and store in session.     |                                     |
| 10  |         Dark Mode Preference Middleware          |        Read a cookie or header and store theme preference in session.   |                                     |
| 11  |         API Rate Limiter                         |        Track request count per user/IP in cache and limit requests.     |                                     |
| 12  |         GeoIP Middleware                         |        Detect country from IP and store for later use (GeoIP libs).     |                                     |
| 13  |         Session Extension Middleware             |        Reset session expiry on every request (keep-alive effect).       |                                     |
| 14  |         Header Injection Middleware              |        Inject security headers (e.g., CSP, X-Frame-Options).            |                                     |
| 15  |         Login Time Tracker                       |        Track time since login and add to request object.                |                                     |
| 16  |         Custom Request Attribute                 |        Add custom data to the request object for views to access.       |                                     |
| 17  |         Referrer Tracker                         |        Save the HTTP referer to session or database.                    |                                     |
| 18  |         Request Path Logger                      |        Log all accessed paths and store in a DB model.                  |                                     |
| 19  |         Error Masker                             |        Catch exceptions and return generic error messages (use with caution).|                               |
| 20  |         Response Size Logger                     |        Log the size of the response body in bytes.                      |                                     |





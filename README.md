Django Project:

# Travel Booking Web Application

A simple travel booking web application built with **Django** that allows users to browse travel options (flights, trains, buses), book tickets, and manage their bookings. The frontend uses **Django templates** and **Bootstrap** for styling.

## 🚀 Live Demo  
You can check out the deployed project here:  
👉 [Travel Booking App](https://shamithajain.pythonanywhere.com/)

---

## Features

### User Management
- User registration, login, and logout using Django's built-in authentication.
- Profile update functionality.

### Travel Options
- Model includes Travel Type (Flight, Train, Bus), Source, Destination, Date & Time, Price, and Available Seats.
- Users can filter travel options by type, source, destination, and date.

### Booking System
- Users can book a travel option by selecting the number of passengers.
- Booking model stores: Booking ID, User, Travel Option, Number of Seats, Total Price, Booking Date, and Status.
- Users can view current and past bookings.
- Users can cancel bookings.

### Frontend
- Responsive pages using **Bootstrap 5**.
- User-friendly interface for browsing travel options, booking, and managing bookings.

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/ShamithaJain/Travel-Booking.git
cd Travel-Booking

```
Create and activate a virtual environment
```
python -m venv venv
```
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

Install dependencies
```
pip install -r requirements.txt
```

Apply migrations
```
python manage.py migrate
```

Create a superuser (optional, for admin access)
```
python manage.py createsuperuser
```

Run the development server
```
python manage.py runserver
```

Open your browser at http://127.0.0.1:8000/.

Usage

Register/Login: Create an account or log in to access booking features.

Browse Travel Options: Filter by travel type, source, destination, and date.

Book a Travel Option: Enter the number of passengers and confirm booking.

View My Bookings: See current and past bookings and cancel if needed.

Profile: Update your user profile information.

Database

Default: SQLite (development)

Recommended for production: MySQL

Deployment

Can be deployed on PythonAnywhere, AWS Elastic Beanstalk, Heroku, or any cloud server.

Make sure to configure the .env file for secret keys and database credentials.

Project Structure
```
travel_booking/
├─ bookings/            # Django app
│  ├─ migrations/       # Database migrations
│  ├─ templates/        # HTML templates
│  ├─ admin.py
│  ├─ forms.py
│  ├─ models.py
│  ├─ urls.py
│  ├─ views.py
│
├─ travel_booking/       # Project settings
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  ├─ asgi.py
│
├─ db.sqlite3            # Local SQLite database (ignored in git)
├─ manage.py
├─ requirements.txt
└─ README.md
```
.gitignore Highlights

Virtual environments: venv/

Database files: *.sqlite3, db.sqlite3

Cache & compiled files: __pycache__/, *.pyc

Media/static files: media/, staticfiles/

IDE configs: .vscode/, .idea/

Environment variables: *.env

Tech Stack

Backend: Python, Django

Frontend: HTML, CSS, Bootstrap

Database: SQLite (dev), MySQL (prod)

Version Control: Git, GitHub

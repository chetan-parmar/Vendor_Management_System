# Vendor_Management_System

The Vendor Management System with Performance Metrics is a Django-based web application designed to manage vendor profiles, track purchase orders, and calculate vendor performance metrics. This system provides an efficient solution for businesses to handle vendor-related activities.

### Table of Contents

- [Vendor Management System](#vendor-management-system)
  - [Key Features](#key-features)
  - [Installation](#installation)

## Key Features
- **User Authentication:** Utilize JWT authentication for secure user and authentication.
- **Serializers:** Use serializers to transform complex data types into JSON and simplify data handling in your Django application.
- **Viewsets:** Implement viewsets to organize the logic for processing HTTP requests in a clean and modular way.
- **Routing:** Define URL patterns and routing mechanisms to map HTTP requests to the appropriate viewsets.
- **Swagger Documentation:** Utilize Swagger to automatically generate interactive API documentation, showcasing the available endpoints and their functionalities.

## Installation
Follow these steps to set up and run the project on your system:

1. Clone the Repository:
- github link https://github.com/chetan-parmar/Vendor_Management_System/tree/main
- git clone <clone_repository >
- Create virtual env .
- Activate the virtual env.
- Go to Project Directory  `cd Vendor_Management_System/vendor_management_system`
- Install all packages from requirements.txt file  using this command `pip install -r requirements.txt`

2. Command to create database table and apply migrations 
- `python manage.py makemigrations`
- `python manage.py migrate`

3. Command to create admin or super user for django admin panel

- `python manage.py createsuperuser`

4. To run project type command:
- `python manage.py runserver`

5. To run test cases type command:
- `python manage.py test app.tests`
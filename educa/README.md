# Educa: Building an E-Learning Platform

## Overview

This project is developed as part of the book "Django 4 by Example". It focuses on building a comprehensive e-learning platform that supports various types of course content and student enrollment. The application uses Django's robust features to create a flexible content management system and an efficient authentication mechanism for users.

## Key Concepts Covered

- **Data Fixtures**: Utilization of fixtures to provide initial data for models.
- **Model Inheritance**: Creation of a flexible system to manage different types of content for course modules.
- **Custom Model Fields**: Implementation of custom model fields on order objects.
- **Authentication System**: Development of an authentication system for the e-learning platform.
- **Content Management System (CMS)**: Use of class-based views and mixins to manage course contents.
- **Groups and Permissions**: Restriction of access to views using Django groups and permissions.
- **Formsets**: Implementation of formsets to edit course content.
- **Drag-and-Drop Functionality**: Creation of a drag-and-drop interface to reorder course modules and their content using JavaScript and Django.
- **Student Registration and Enrollment**: Development of a system for student registration and management of course enrollments.
- **Content Rendering and Caching**: Techniques for rendering different kinds of content and caching using Django’s cache framework.


## Additional Features

- **Security Enhancements**: Implementation of a robust authentication system and restricted access using groups and permissions.
- **Template Integration**: Utilization of Django's template inheritance to streamline the user interface.
- **Administration Customization**: Customization of the Django admin site for enhanced usability.
- **Dynamic Course Content Management**: Use of formsets and drag-and-drop functionality for flexible content management.

## Technologies Used

- **Django 4**: Leveraging the latest features of Django 4 to build a robust e-learning platform.
- **JavaScript**: Implementing dynamic drag-and-drop functionality for course content management.
- **Django Groups and Permissions**: Using Django’s built-in groups and permissions system to secure access to different views and functionalities.
- **Redis and Memcached**: Implementing caching mechanisms to improve performance.

## Running the Project

To run this project locally:

1. Ensure you have Python, Django, and Docker installed.
2. Clone the repository to your local machine.
3. Create and start the Redis service using Docker:
    ```sh
    docker-compose up -d redis
    ```
4. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```
5. Apply database migrations:
    ```sh
    python manage.py migrate
    ```
6. Start the Django development server:
    ```sh
    python manage.py runserver
    ```
7. Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser to access the application.


## Monitoring Redis with Django Redisboard

You can monitor your Redis server using Django Redisboard. Django Redisboard adds Redis statistics to the Django administration site. You can find more information about Django Redisboard at [https://github.com/ionelmc/django-redisboard](https://github.com/ionelmc/django-redisboard).

Run the development server and open [http://127.0.0.1:8000/admin/redisboard/redisserver/add/](http://127.0.0.1:8000/admin/redisboard/redisserver/add/) in your browser to add a Redis server to monitor. Under the Label, enter `redis`, and under URL, enter `redis://localhost:6379/0`. Click on SAVE. The information will be saved to the database, and you will be able to see the Redis configuration and metrics on the Django administration site.

# MyShop Application with Django 4

## Overview

This project is developed as part of the book "Django 4 by Example". It focuses on building a functional e-commerce platform that supports session-based shopping carts and order placement. The application uses Django's robust features alongside Celery for handling asynchronous tasks, leveraging RabbitMQ as the message broker.


## Key Concepts Covered

- **E-commerce Fundamentals**: The creation of a product catalog and a dynamic shopping cart that persists across user sessions.
- **Asynchronous Task Processing**: Utilizing Celery with RabbitMQ to manage background tasks such as order processing.
- **Context Processing**: Implementing a custom context processor to make the shopping cart globally available across all templates.
- **Order Management**: Developing a form for handling order placements within the application.


## Additional Features

- **Security Enhancements**: Instructions for securing RabbitMQ in production by managing user roles and permissions.
- **Template Integration**: Demonstrating Django’s template inheritance to streamline the user interface.


## Technologies Used

- **Django 4**: Utilizing the latest features of Django 4 to build robust web applications.
- **Celery**: Implementing asynchronous task queues to improve application performance.
- **RabbitMQ**: Employing RabbitMQ as a message broker to manage communications between the application and Celery.


## Running the Project

To run this project locally:

1. Ensure you have Python, Django, and Django Extensions installed.
2. Clone the repository to your local machine.
3. Run `python manage.py migrate` to apply database migrations.
4. Start the server with `python manage.py runserver`.
5. To run the server securely through HTTPS, use this command: `python manage.py runserver`.
6. Navigate to `http://127.0.0.1:8000/` in your web browser to access the application.


## Running RabbitMQ with Docker

To run RabbitMQ in a Docker container:

```bash
docker pull rabbitmq
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
```

## Accessing RabbitMQ’s management interface

Open ` http://127.0.0.1:15672/ ` in your browser. You will see the login screen for the management UI of RabbitMQ.

Enter ` guest ` as both the username and the password and click on Login.

> If you use RabbitMQ in a production environment, you will need to create a new admin user and remove the default guest user. You can do that in the Admin section of the management UI.

## Running Celery worker

Make sure RabbitMQ is running !
Open a shell and start a Celery worker from the project directory, using the following command:

```bash
celery -A core worker -l info
```

## Monitoring Celery with Flower

Make sure ` flower ` is installer (see the requirements.txt), you can launch Flower by running the following command in a new shell from your
project directory:

```bash
celery -A core flower
```

Open ` http://localhost:5555/dashboard ` in your browser. You will be able to see the active Celery workers and asynchronous task statistics.

## Why using asynchronous tasks

Use asynchronous tasks not only for time-consuming processes, but also for other processes that do not take so much time to be executed but that are subject to connection failures or require a retry policy.


## Conclusion

This project provides a comprehensive guide to building a secure and functional authentication system using Django 4, demonstrating the framework's capabilities in handling user-centric processes, custom user models, and integrating modern authentication mechanisms like social logins.


## Screen shots

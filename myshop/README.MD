# MyShop Application with Django 4

## Overview

This project is developed as part of the book "Django 4 by Example". It focuses on building a functional e-commerce platform that supports session-based shopping carts and order placement. The application uses Django's robust features alongside Celery for handling asynchronous tasks, leveraging RabbitMQ as the message broker.


## Key Concepts Covered

- **E-commerce Fundamentals**: Creation of a product catalog and a dynamic shopping cart that persists across user sessions.
- **Asynchronous Task Processing**: Utilization of Celery with RabbitMQ to manage background tasks such as order processing.
- **Context Processing**: Implementation of a custom context processor to make the shopping cart globally available across all templates.
- **Order Management**: Development of a form for handling order placements within the application.
- **Payment Integration**: Integration of the Stripe payment gateway to process transactions securely.
- **Webhook Handling**: Creation of a webhook endpoint to receive and handle payment notifications from Stripe.
- **Coupon system**: Creation of a coupon system using Django sessions and integrated it with Stripe.
- **Recommendation engine**: Creation of a recommendation engine using Redis to recommend products that are usually purchased together.

## Additional Features

- **Security Enhancements**: Instructions for securing RabbitMQ in production by managing user roles and permissions.
- **Template Integration**: Demonstration of Django’s template inheritance to streamline the user interface.
- **Administration Customization**: Customization of the Django admin site with specific views and templates for enhanced usability.
- **Order Export to CSV**: Development of a custom administration action to export order data to CSV files.
- **PDF Generation**: Learning how to generate PDF files with WeasyPrint and attach them to emails for order confirmations or receipts.


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


## Running Redis

Redis is used for the recommendation engine:

```bash
docker run -it --rm --name redis -p 6379:6379 redis
```


## Why using asynchronous tasks

Use asynchronous tasks not only for time-consuming processes, but also for other processes that do not take so much time to be executed but that are subject to connection failures or require a retry policy.


## Conclusion
🤔

## Screen shots

### RabbitMQ dashboard

<img width="926" alt="Capture d'écran 2024-05-08 175826" src="https://github.com/SaiedZ/django-4-by-example/assets/90851774/ef315163-b2db-4f88-841d-f16feae6e80a">


### Flower dashboard

![Capture d'écran 2024-05-08 175925](https://github.com/SaiedZ/django-4-by-example/assets/90851774/442a5801-e2cf-489b-9a1e-a55756481e73)


### Site

<img width="895" alt="Capture d'écran 2024-05-08 180710" src="https://github.com/SaiedZ/django-4-by-example/assets/90851774/7c1ee23d-e230-4fe6-9851-f70e95f5a26a">
<img width="904" alt="Capture d'écran 2024-05-08 180744" src="https://github.com/SaiedZ/django-4-by-example/assets/90851774/7d9b8e71-5c60-406b-aedd-3f3bce4ae4e1">
<img width="904" alt="Capture d'écran 2024-05-08 180744" src="https://github.com/SaiedZ/django-4-by-example/assets/90851774/7a8e6df1-2b33-4b97-8094-584c8aa25a16">

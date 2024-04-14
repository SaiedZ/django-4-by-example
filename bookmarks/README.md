# Bookmarks Application with Django 4

## Overview

This project is developed as part of the book "Django 4 by Examples". It focuses on creating a robust authentication system for a website, allowing users to register, log in, log out, manage their profiles, and utilize social authentication with existing Facebook, Twitter, or Google accounts. The chapter also explores the creation of a custom user model, a custom authentication backend, and serving the development server through HTTPS.

## Key Concepts Covered

- **User Authentication**: Implementation of a full user authentication system, including registration, login, logout, and social login functionalities using OAuth 2.0.
- **Custom User Model**: Creation of a custom user model that extends Django's default `User` model to include additional fields and functionalities.
- **Authentication Views**: Development of views for handling user authentication processes such as registering, logging in, logging out, editing passwords, and resetting passwords.
- **Custom Authentication Backend**: Designing and implementing a custom authentication backend to allow users to use their email addresses for logging in instead of a username.
- **Social Authentication**: Integration of social login options using Python Social Auth to leverage OAuth 2.0 for authorization with platforms like Facebook, Twitter, and Google.
- **User Profiles**: Automatic creation of user profiles during social login and allowing users to edit their personal information after registration.
- **Password Management**: Integration of Django's built-in views and forms for password change and reset functionalities.

## Additional Features

- **Email as Username**: Customization of the authentication process to use email addresses as the primary identifier for logging in, enhancing the user experience and aligning with modern web practices.
- **Profile Management**: Development of a system where users can manage and update their profile information, promoting user engagement and personalization.

## Technologies Used

- **Django 4**: Utilizing the latest features of Django 4 to build a secure and efficient authentication system.
- **Python Social Auth**: Facilitating social authentication using industry-standard OAuth 2.0 protocols.

## Running the Project

To run this project locally:

1. Ensure you have Python, Django, and Django Extensions installed.
2. Clone the repository to your local machine.
3. Run `python manage.py migrate` to apply database migrations.
4. Start the server with `python manage.py runserver`.
5. To run the server securely through HTTPS, use this command: `python manage.py runserver_plus --cert-file cert.crt`.
6. Navigate to `http://127.0.0.1:8000/` in your web browser to access the application.

## Conclusion

This project provides a comprehensive guide to building a secure and functional authentication system using Django 4, demonstrating the framework's capabilities in handling user-centric processes, custom user models, and integrating modern authentication mechanisms like social logins.

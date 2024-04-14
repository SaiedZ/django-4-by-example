# Bookmarks Application with Django 4

## Overview

This project is developed as part of the book "Django 4 by Examples". It focuses on creating a robust authentication system for a website, allowing users to register, log in, log out, and manage their profiles. The chapter also explores the creation of a custom user model and a custom authentication backend to allow users to log in using their email addresses.

## Key Concepts Covered

- **User Authentication**: Implementation of a full user authentication system, including registration, login, and logout functionalities.
- **Custom User Model**: Creation of a custom user model that extends Django's default `User` model to include additional fields and functionalities.
- **Authentication Views**: Development of views for handling user authentication processes such as registering, logging in, logging out, editing passwords, and resetting passwords.
- **Custom Authentication Backend**: Designing and implementing a custom authentication backend to allow users to use their email addresses for logging in instead of a username.
- **User Profiles**: Building models and views to handle user profiles, allowing users to edit their personal information after registration.
- **Password Management**: Integration of Django's built-in views and forms for password change and reset functionalities.

## Additional Features

- **Email as Username**: Customization of the authentication process to use email addresses as the primary identifier for logging in, enhancing the user experience and aligning with modern web practices.
- **Profile Management**: Development of a system where users can manage and update their profile information, promoting user engagement and personalization.

## Technologies Used

- **Django 4**: Utilizing the latest features of Django 4 to build a secure and efficient authentication system.

## Running the Project

To run this project locally:

1. Ensure you have Python and Django installed.
2. Clone the repository to your local machine.
3. Run `python manage.py migrate` to apply database migrations.
4. Start the server with `python manage.py runserver`.
> to run server the site through ` HTTPS ` use this command: `python manage.py runserver_plus --cert-file cert.crt`
5. Navigate to `http://127.0.0.1:8000/` in your web browser to access the application.

## Conclusion

This chapter provides a comprehensive guide to building a secure and functional authentication system using Django 4, demonstrating the framework's capabilities in handling user-centric processes and custom user models.

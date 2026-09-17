# Library Management System

## Project Overview

The Library Management System is a CRUD-based web application developed using Django, Django REST Framework, HTML, CSS and JavaScript.

The system helps manage library book records in a simple and organized way.

## Problem Statement

Managing book records manually can be time-consuming and may lead to errors.

This project provides a digital system to add, view, update and delete book records easily.

## Objectives

* To create a simple library management application.
* To implement CRUD operations.
* To store book details in a database.
* To provide REST API support.
* To validate user input.
* To provide a simple and responsive user interface.

## Technologies Used

* HTML
* CSS
* JavaScript
* Python
* Django
* Django REST Framework
* SQLite
* Git and GitHub

## Main Features

* Add new books
* View all books
* Edit book details
* Delete books
* Search books by title, author or ISBN
* Input validation
* REST API
* Database storage

## Book Details

Each book contains:

* Book ID
* Title
* Author
* ISBN
* Availability status

## CRUD Operations

| Operation | Description         |
| --------- | ------------------- |
| Create    | Add a new book      |
| Read      | View book records   |
| Update    | Modify book details |
| Delete    | Remove book records |

## API Endpoints

```text
GET     /api/books/
POST    /api/books/
GET     /api/books/{id}/
PUT     /api/books/{id}/
PATCH   /api/books/{id}/
DELETE  /api/books/{id}/
```

## Project Structure

```text
Library_Management_System/
│
├── books/
│   ├── migrations/
│   ├── templates/
│   │   └── index.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── library_system/
├── db.sqlite3
└── manage.py
```

## How to Run

1. Install Python.
2. Install Django and Django REST Framework.
3. Open the project folder in VS Code.
4. Run:

```bash
python manage.py migrate
```

5. Start the server:

```bash
python manage.py runserver
```

6. Open the application:

```text
http://127.0.0.1:8000/
```

## Testing

The application was tested for:

* Create operation
* Read operation
* Update operation
* Delete operation
* REST API functionality
* Database storage
* Search functionality
* Input validation

## Future Enhancements

* User login and authentication
* Book issue and return management
* Student/member management
* Due date and fine calculation
* Advanced search and filtering
* Improved dashboard
* Cloud database integration

## Conclusion

The Library Management System successfully implements a CRUD-based web application using Django, REST API, SQLite database and a web-based frontend.

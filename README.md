# Django Error Middleware

* A Django Middleware which intercepts each HTTP response and if any error occurs it logs it into database along with request and response.


## PreRequisites

* [Python3.6](https://www.python.org/downloads/)
* [Flask-Sqlalchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - pip3 install django
* [djangorestframework](https://www.django-rest-framework.org/) - pip3 install djangorestframework


### How to run the project

$ python3 manage.py runserver


### About the Database

* ErrorStack
    request: Request stored as string
    response: Response stored as string
    method: Request METHOD
    error: Request status_code
    error_stack: Request Message
    created_date: Date database object was created
    modified_date: Date database object was modified


### APIs

#### 1. GET [/error_stack/](http://127.0.0.1:8000/error_stack/)

* READ data using search or id

#### 2. POST [/error_stack/](http://127.0.0.1:8000/error_stack/)

* CREATE object

#### 3. PUT [/error_stack/](http://127.0.0.1:8000/error_stack/)

* UPDATE an object using id

#### 4. DELETE [/error_stack/](http://127.0.0.1:8000/error_stack/)

* DELETE specific object using id

### Postman Collection for the above APIs

[https://www.getpostman.com/collections/c2923a1087ea613e4ad4](https://www.getpostman.com/collections/c2923a1087ea613e4ad4)
# Chirpey

### Description & Problem Statement

Problem was to make Micro-blogigng clone where user can register and can share thoughts as Post.

This app is based on REST API built using Django and DjangoRestFramework which support basic CRUD Operations.

Tech Stack:
```
Python
Django
Django Rest-framework
Postgres
Simple-JWT
Swagger
Redis
```

In this current version of the project, I have made APIs for user to register, login , get profile details,update 
profile details, add a post, update and delete the post, get all the post on timeline and logout of the application.

Alongside the user APIs, the `login` and `logout` APIs are also available in addition to the user APIs to obtain 
authorization tokens.

Regarding `Authorization` and `permissions`, I have used `Bearer` & `JWT` to validate user request and certain 
permissions classes of rest_framework are used to authorize the request.

---

### Prerequisties
To run this project on a machine, we need `Python` and `Postgres` database as basic requirements.

#### Install Steps
- First and foremost, start by creating a virtual environment the current directory. I have used `venv` as the name 
  of the virtual environment.
```python
python -m venv virtual
```
- Now, install redis server for on local machine, verify if it is working. This will be used for caching later.
```shell
sudo apt-get install redis-server
redis-cli -v
redis-cli
```
- Once done with the installation, navigate to the virtual environment and activate it(below is for linux).
```shell
source virtual/bin/activate
```
- Now install all the dependencies using pip and `requirement.txt` file.
```python
pip install -r requirement.txt
```

Now that dependencies are ready, proceed to set up the project.

### Setup & Intitial Steps

- Create a django-project using `django-admin`, post that you will get to see some  configuration files
```shell
django-admin startproject applo
```
- Change directory to `applo` and start your new app(perform this to create any new app)
```shell
django-admin statapp mod_apps
```
- Install django-redis in virtual environment 
```python
pip install django-redis
```

- This project uses `.env` file to store all our secret keys, so create a `.env` file and store following variables. 
  Make sure to connect `.env` file to settings.py. Google it!!
```.dotenv
DB_NAME={your database name}
DB_USER={your database user's name}
DB_PASSWORD={your database user's password}
DB_HOST=127.0.0.1 or {url of database if using remote databse}
DB_PORT=5432
```
- Configuration for Redis in settings.py
```
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://localhost:6379/0',  # Replace with your Redis configuration
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    },
}
```

- As we are using DjangoRestFramework, make sure to add `'rest_framework'` in INSTALLED_APPS in settings.py of your 
  project. `drf-yasg` is used for using swagger, do add it to.
```python
INSTALLED_APPS = [
    'drf_yasg',
    'rest_framework',
]
```

- After this is done, we migrate our model
```shell
python3 manage.py migrate
```

- Now that migration is done, we are ready to run our application

```shell
python3 manage.py runserver
```

- You can create a superuser/admin user and provide all the details required afterwards. This superuser will server as an admin to add and manage android apps.
```shell
./manage.py createsuperuser 
```
---

### Usage

#### Endpoints

- The resources/Endpoints provided in this project are as follows: 
```
- /api/users/register/ - for user to register
- /api/users/login/ - for user to login
- /api/users/profile/ - for user to get the profile details
- /api/users/update/ - for user to update any details on profile
- /api/users/logout/ - for user to logout

- /api/posts/ - user adds new post
- /api/posts/<inr:post_id> - post details are fetched using post_id, patch and delete request is also served
- /api/posts/list/ - lists all posts on the platform

- /swagger/ - to check for swagger documented APIs

```
- `/api/users/login/`, `/api/users/register/` do not require any authentication or authorisation, but 
  all other endpoints requires authentication.
- Once we create a user, we can send a `POST` request to `/account/login/` to get `access` and `refresh` token for both admin and user.
- Now we can use this `access` token as `Bearer ${access}` as `Authorization` header in our request.
- <user_id> will be obtained from the token in the request and used. Appropriate permissions and error checks are 
applied to authenticate and Authorize the user during the CRUD operations.
- All the Validations errors, Integrity errors are handled properly and responses are received as 
rest_framework.response format.




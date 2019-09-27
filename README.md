# tk-django or TourKenya-API
Tk or TourKenya is a kenyan tourism application. It allows users who have visited game parks and reserves in Kenya to share their experiences to others by writing articles on their visits.


#### Getting Started
Go to https://github.com/Darius-Ndubi/tk-django.git
Download or clone the repository to your local machine. 
Open the project using your favorite IDE

----
#### Prerequisites
 - Python3.
 - Virtual environment.
 - Django
 - Docker
 - Postman or insomnia
 - Postgres
 - Browser e.g Chrome, firefox

#### Application requirements
Create a .env_sample and in it add:
  - DATABASE_NAME=db_name
  - DATABASE_USER=db_owner
  - DATABASE_PASSWORD=db_user_password
  - DATABASE_HOST=db_host
  - DATABASE_PORT=db_port

    Local Environment
     - SECRET_KEY='Applications_secret_key'
     - APP_DEBUG_MODE=App_debug_mode

    Docker Environment 
    - DEBUG_MODE=App_debug_mode
    - DEVELOPMENT_SECRET_KEY='Applications_secret_key'
 
 Save the file.

 ----
#### Setting up without docker
Navigate to your project folder and open it using the terminal.
Create a virtual environment. *virtualenv name_of_virtual_environment preferably `tk`.
Folder with the 'name_of_virtual_environment' will be created and that is our environment.
Clone this repo to your local computer using git clone https://github.com/Darius-Ndubi/tk-django.git
Activate the environment via `source tk/bin/activate. Switch into the project directory. 
run source .env_sample
Install the project's dependencies by running pip install -r requirements.txt
Initialize the app migrations with `python manage.py makemigrations` run migrations with `python manage.py migrate`
Start the development server with the command `python manage.py runserver`

To stop the development server run `Ctrl+C` command on the terminal running the server.
  

#### Setting up with docker [Most preferred due the uniformity offered using this environment]
Navigate to your project folder and open it using the terminal.
Install docker 
[Link](https://docs.docker.com/install/)
Use the documentation to install docker on your machine. Always works.
Clone the repository https://github.com/Darius-Ndubi/tk-django.git
Change Directory into tk-django. Setup the .env file following directives from  sample.env file or Steps above.
*run* `docker-compose build` to build the development image. This takes some time. 😅 :sweat_smile:
*then* `docker-compose up` to start up the application in docker development environment

To stop the development server run `Ctrl+C` command on the terminal running the server. 


#### Postman or Insomnia
API Routes. 
Endpoints available for this api are shown in the table below:

````
| Requests    |   EndPoint                     | Functionality              | Fields
| ----------- |:------------------------------:| --------------------------:|
|  POST       |  /api/signup/                  | New user signup            | eg {"email": "string@user.com","firstName": "string123","lastName": "string123",  "username": "stranger","password": "string123"
}
|  POST       |   /api/signin/                 | Known user signin          | eg {"email": "string@user.com","password":"string123"}
|   GET       |   /api/articles/               | Get all tour articles      |
|  POST       |   /api/article/create/         | Add a tour article         | eg{"title": "string,"body": "string","draft":"Boolean","posted":"Boolean"}
|  GET        |  /api/article/article_id/      | Get specific article       |
|  DELETE     | /api/article/article_id/delete/| User delete specificarticle|
|  PUT        | /api/article/article_id/update/| User update specificarticle| eg{"title": "string,"body": "string","draft":"Boolean","posted":"Boolean"}
````
 
Test the API on postman or insomnia
 
 #### Built with Love using

* python 3.6.9
* Django
* Django Rest Framework
* Postgres DB

*********

#### Versioning
Most recent version: [version 2](https://tourkenya-staging.herokuapp.com/api/signup/) but [Version 1](http://tourkenya.herokuapp.com/) done with Flask-Templates and MYSQL DB.

***

#### Authors
Darius Ndubi
 
 PS: This is the Minimum Viable Product [MVP] of TourKenya. :grin: :grin:

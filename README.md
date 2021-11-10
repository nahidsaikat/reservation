# Room Reservation Application

This application is to allow the employee to reserve meeting room so that the 
meeting room is not already occupied by others.
Following are the features this application has,

* Create employee
* Create room
* Create room reservation
* Cancel room reservation
* Filter room reservation by employee
* Authentication to perform above operations


## Run the application
Before running the application please ensure that following are available
in the system,
* docker
* docker compose
* postgresql

After that run this command
* `mkdir -p .docker/data/postgres_data`
* `make up`
* `make superuser` (Create a super user by providing email and password)
 
The application will be running on `http://localhost:8100/`


## Instructions for development environment
For the development you will need to have `pyenv` and `pipenv` already installed.
Follow the steps below,
* `git clone https://github.com/nahidsaikat/reservation.git`
* `cd reservation`
* `mkdir -p .docker/data/postgres_data` (This will require if you use docker compose or makefile)
* `pipenv install`
* `pipenv shell`
* `python manage.py migrate`
* `python manage.py runserver`
* `python manage.py test`    (To run the test)


## Dependencies
* PostgreSQL 14.0
* Python 3.10
* Django 3.2.9
* DRF 3.12.4

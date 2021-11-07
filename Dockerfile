# pull official base image
FROM python:3.10.0

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /app/Pipfile
RUN pipenv install --skip-lock --dev

# copy project
COPY . /usr/src/app/

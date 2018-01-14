pollApp
=========

# Installation

## Install OS (Ubuntu) Requirements

	sudo apt-get update
	sudo apt-get upgrade

## Clone Project

	git clone https://github.com/sharmaadarsh563/pollApp.git pollApp

## Create Virtual Envirnoment

	virtualenv env
	source env/bin/activate

## Install Project Requirements

	pip install -r requirements.txt

## Setup Postgres

    sudo apt-get install postgresql
	pip install psycopg2
	sudo su postgres
	psql -d template1 -U postgres
	CREATE USER your-username WITH PASSWORD your-password;
	CREATE ROLE poll_app;
	GRANT poll_app TO your-username;
	CREATE DATABASE pollApp_db OWNER your-username;
	\c pollApp_db
	\i path-to-psql-dump-data
	\q
	psql -d pollApp_db -U your-username

## Create a superuser

	python manage.py createsuperuser

## Run the Development Server

	python manage.py runserver

**Note:** Never forget to enable virtual environment (`source env/bin/activate`) before running above command and use settings accordingly.

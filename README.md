# Counterpart - The Challenge

We're going to create a system that will use the **USGS Earthquake** public data set to show us where the nearest earthquake above a 5.0 was in relation to one of the following cities, between 2 dates that the user specifies:
* Los Angeles, CA
* San Francisco, CA
* Tokyo, Japan

The result returned should show something like:

**Result for Los Angeles between June 1 2021 and July 5 2021 : The closest Earthquake to Los Angeles was a M 5.7 - South of Africa on June 30**

The application should also save the results every time we run the search, and allow us to view the results again as quickly as possible.
If no results were found during those dates, simply show a "No results found"

**The system will consist of the following:**

* An endpoint to create a new city
* An endpoint for us to search for earthquakes
    * Including
        * A start date for the search
        * A end date for the search
    * A results JSON of current results of the search

This project should form the basis of how you would approach building a real app and backend where this data was needed by our team.
We don't expect you to spend more than 1 hour on this.

## Things we look for
We know this is something of a toy challenge, but we've found writing "real" code is very helpful in seeing how someone actually works and thinks.
* **Correctness:** How well does your code adhere to the specifications.
* **Implementation**: How are you storing the data? Are you caching it, or running the query
every request? What are you using for data storage?
* **Documentation:** Can we easily set this up ourselves? Do you call out your assumptions
and your tradeoffs?

Feel free to use any packages such as scipy, numpy, etc to help with the challenge.

## Requirements
* **Language/framework choice:** For this challenge please use **Python**.
    * You can display the results in anyway you like, however, bonus points if you use a frontend framework like React or Vue Js (optional)
    * **Database:** Feel free to use any database for this challenge

## Data Set

USGS provides urls for you to query from them for free here:
https://earthquake.usgs.gov/earthquakes/search/
An example of using the URL:
https://earthquake.usgs.gov/fdsnws/event/1/query.geojson?starttime=2021-06-07&endtime=202 1-07-07&minmagnitude=4.5&orderby=time


# Backend
> **Note**
For the development, I followed the Django-Styleguide proposed by the company [HackSoft](https://github.com/HackSoftware/Django-Styleguide).

Developers Setup
================

services with docker except the API (Django), since it is more comfortable to debug outside the container.

First, we run the services with docker, then Django.

Services with Docker (Database)
------------------------------ 
    ~$ docker-compose build
    ~$ docker-compose up -d

API
---

Environment Variables

    ~$ cp .env.example .env

Install Poetry

    ~$ curl -sSL https://install.python-poetry.org | python3 -
    ~$ export PATH="$HOME/.local/bin:$PATH"

Install dependencies

    ~$ poetry install

Run migrations

    ~$ poetry run python manage.py migrate

Initial Data
    ~/ poetry run python3 manage.py loaddata main/fixtures/initial_data.json 

Run runserver

    ~$ poetry run python manage.py runserver 0.0.0.0:9000

Run tests

    ~/ poetry run python3 manage.py test


## Endpoints

You can use the [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client) extension for VSCode or use postman.

Thunder Client files [here](./thunder-tests/)
Postman File [here](./thunder-collection_API_postman.json)

# Quexl

![Build Status](https://github.com/TeamoreA/r-backend/workflows/Python%20application/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This is an online marketplace for your local comodities.


The Application has been documented using Postman Documentation tht can be viewed [here.](https://documenter.getpostman.com/view/5990083/TVRn4n3Z)

## Setting Up the Application Locally

### Installing PostgreSQL

- PostgreSQL server is required by the application for the application to run. To use the local PostgreSQL server, ensure you have PostgreSQL [installed](https://www.postgresql.org/docs/12/tutorial-install.html) and running. ensure you add the server PostgreSQL connection URL to your .env file

    ``` bash
    DATABASE_URL=postgres://<user>:<password>@<host>:<port>/<database name> #  postgres://postgres@127.0.0.1:5432 if no username or password configured, or just a remote host's URL
    ```

### Setup VirtualEnvironment

- Setup Pyhton virtual environment by running `python3 -m venv venv`

- Activate the virtual environment by running `source venv/bin/activate`

### Install Application Dependencies

- Run the following command to install application dependencies `pip install -r requirements.txt`

- After installing the dependencies, add the necessary environmental variables required by the application. Sample environmental varials are:

    ```bash
    DEBUG=True
    DATABASE_URL=postgres://<user>:<password>@<host>:<port>/<database name>
    SECRET_KEY="611=df5*i4evgbpu3)$th%=##=kw#h#@8zomsn1$eo6f^uv74$" # sample SECRET_KEY
    ```

- Add the above variables in a file name `.env` in the root of the project

### Perform Initial Migrations

- To ensure that the database tables are properly configured, run migrations by running `./manage.py migrate` at the root of the project

### Start the Server

- After successfully performing migrations, the server can be started by running `./manage.py runserver` at the root of the project


### Contributing

- Before contributing, ensure to install `pre-commit` by running  in the root of the application after application setup.
    ``` bash
    $ pre-commit init
    ```
    This is to enforce coding styles.

## Deployments and Releases

- The project had been deployed to Heroku. To view the various versions of the deployed apps, go [here](https://github.com/TeamoreA/r-backend/deployments)

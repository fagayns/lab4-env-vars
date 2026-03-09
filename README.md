Flask App with Environment Variables and Docker

## Description
This is a simple Flask application that demonstrates the correct use of environment variables for configuration.
Several environments are supported: development and production.
Secrets and configuration parameters are stored in .env files and securely uploaded to the application.

## Project objectives

-Create a Flask application with configuration via environment variables (env vars).
-Create separate ones .env files for development and production.
-Properly handle secrets (for example, SECRET_KEY).
-Create a Dockerfile with support for environment variables.
-Run the application in different modes.
## Structure of the project
flask-env-app/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── config.py
│
├── .env.dev
├── .env.prod
├── Dockerfile
├── requirements.txt
└── README.md

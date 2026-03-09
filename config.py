import os
from dotenv import load_dotenv

env = os.getenv("APP_ENV", "development")

if env == "development":
    load_dotenv(".env.development")
else:
    load_dotenv(".env.production")


class Config:
    APP_ENV = os.getenv("APP_ENV")
    DEBUG = os.getenv("DEBUG") == "true"

    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    SECRET_KEY = os.getenv("SECRET_KEY")

    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

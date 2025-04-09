from .base import *

DEBUG = True

DATABASES = {
    "default": {
        # "ENGINE": "django.db.backends.postgresql_psycopg2",
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USERNAME"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    },
    # "postgres": {
    #     "ENGINE": "django.contrib.gis.db.backends.postgis",
    #     "NAME": "test",
    # },
}

from dj_database_url import parse as db_url
from decouple import config


def default_database():
    default_database_config = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('POSTGRES_NAME', default='postgres'),
        'USER': config('POSTGRES_USER', default='postgres'),
        'PASSWORD': config('POSTGRES_PASSWORD', default='postgres'),
        'HOST': config('POSTGRES_HOST', default='localhost'),
        'PORT': config('POSTGRES_PORT', default=5432)
    }
    has_database_url = config('DATABASE_URL', default=False)
    return config('DATABASE_URL', cast=db_url) if has_database_url else default_database_config

from challenge.settings.dev import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'ec2-54-197-254-189.compute-1.amazonaws.com',
        'PORT': '5432',
        'NAME': 'd7gri73j0fkrn1',
        'USER': 'munevylyepslzv',
        'PASSWORD': '943afb4dfce6193d2b07532fad7fe083306e7900ae4895b41d89f943a106578f',
        'CONN_MAX_AGE': 60
    }
}
## settings.py
import os
import dj_database_url

# other properties

DATABASES = {'default': dj_database_url.config(default=os.environ['DATABASE_URL'], engine='django_cockroachdb')}
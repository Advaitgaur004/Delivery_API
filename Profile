release: python manage.py migrate --no-input
web gunicorn apif.wsgi --log-file -
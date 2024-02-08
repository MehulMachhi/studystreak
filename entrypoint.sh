# !/bin/sh
# Add the following line before starting your Django application
./wait-for-it.sh postres_db:16751 --timeout=15 -- echo "PostgreSQL is ready!"
python3 manage.py migrate --noinput

python3 manage.py collectstatic --noinput
gunicorn lmss.wsgi:application --bind 0.0.0.0:8000


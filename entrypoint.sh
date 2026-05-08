#!/bin/sh

echo "⏳ Waiting for database..."

sleep 5  # Waiting for database to START

echo "🚀 Apply migrations"
python manage.py migrate

echo "📦 Collect static files"
python manage.py collectstatic --noinput

echo "🔥 Start Gunicorn"
gunicorn cyber_portfolio.wsgi:application --bind 0.0.0.0:8000

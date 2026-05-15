#!/bin/bash
echo "==> Upgrading pip..."
python3.14 -m pip install --upgrade pip

echo "==> Installing dependencies..."
python3.14 -m pip install -r requirements.txt

echo "==> Running Database Migrations..."
python3.14 manage.py migrate --noinput

echo "==> Collecting static assets..."
python3.14 manage.py collectstatic --noinput --clear

echo "==> Build process completed successfully!"

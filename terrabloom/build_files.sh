#!/bin/bash
echo "==> Upgrading pip..."
python3.9 -m pip install --upgrade pip

echo "==> Installing dependencies..."
python3.9 -m pip install -r requirements.txt

echo "==> Running Database Migrations..."
python3.9 manage.py migrate --noinput

echo "==> Collecting static assets..."
python3.9 manage.py collectstatic --noinput --clear

echo "==> Build process completed successfully!"

#!/usr/bin/env bash
set -o errexit
echo "Checking if db.sqlite3 exists..."
if [ -f "db.sqlite3" ]; then
    echo "db.sqlite3 found."
else
    echo "db.sqlite3 not found! Creating it..."
    python manage.py migrate
fi
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
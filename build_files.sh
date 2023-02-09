#!/bin/bash
# upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Collect static files
# python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate
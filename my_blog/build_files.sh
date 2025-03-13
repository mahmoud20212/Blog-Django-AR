#!/bin/bash
pip install -r requirements.txt
# python manage.py collectstatic --noinput  # If using static files
python manage.py migrate --noinput       # Apply migrations
#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Current directory: $(pwd)"

# Upgrade pip and install requirements
pip install --upgrade pip
pip install -r requirements.txt

# Make sure gunicorn is installed specifically
pip install gunicorn==23.0.0

# Print debug information
echo "Python version: $(python --version)"
echo "Pip version: $(pip --version)"
echo "Installed packages:"
pip list
echo "Gunicorn location: $(which gunicorn || echo 'Not found in PATH')"
echo "PATH: $PATH"

# Run Django commands
python manage.py collectstatic --no-input
# Uncomment if you need migrations
# python manage.py migrate
#!/usr/bin/env bash
# exit on error
set -o errexit

# Make start.sh executable
chmod +x start.sh

# Debugging information
echo "Current directory: $(pwd)"
echo "User: $(whoami)"
echo "PATH: $PATH"
echo "Python locations:"
find / -name python3 -type f 2>/dev/null | head -n 10
find / -name python -type f 2>/dev/null | head -n 10

# Upgrade pip and install requirements
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn==23.0.0

# Django commands
python manage.py collectstatic --no-input
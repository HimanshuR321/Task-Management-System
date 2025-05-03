import os
import subprocess
import sys

def setup_django_project():
    subprocess.run([sys.executable, "-m", "venv", "venv"])
    
    if os.name == 'nt':
        subprocess.run(["./venv/Scripts/pip", "install", "-r", "requirements.txt"])
        subprocess.run(["./venv/Scripts/django-admin", "startproject", "taskmanager", "."])
        subprocess.run(["./venv/Scripts/python", "manage.py", "startapp", "api"])
    else: 
        subprocess.run(["./venv/bin/pip", "install", "-r", "requirements.txt"])
        subprocess.run(["./venv/bin/django-admin", "startproject", "taskmanager", "."])
        subprocess.run(["./venv/bin/python", "manage.py", "startapp", "api"])

if __name__ == "__main__":
    setup_django_project() 
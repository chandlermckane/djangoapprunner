FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /djangoapprunner/app

RUN python -m venv /djangoapprunner/venv

COPY requirements.txt /djangoapprunner/app/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /djangoapprunner/app/

# The command to run when the container starts
# Example: run Django's development server
# Replace 'myproject.wsgi:application' with your Django project's WSGI application path
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi:application"]

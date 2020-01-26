FROM python:3.7.6-stretch
WORKDIR /django_app
COPY ./Pipfile /django_app/Pipfile
COPY ./Pipfile.lock /django_app/Pipfile.lock
RUN python -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --ignore-pipfile
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

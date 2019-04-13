# last edit 14 Dec 2018 for Heroku

FROM python:3.6
ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt
# EXPOSE 5000
CMD gunicorn --bind 0.0.0.0:5000 wsgi:app
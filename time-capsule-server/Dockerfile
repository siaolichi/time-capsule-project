# last edit 14 Dec 2018 for Heroku

FROM python:3.6
ADD . /app
WORKDIR /app

ADD requirements.txt /app
RUN pip install -r requirements.txt

CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT wsgi:app

# EXPOSE 5000  
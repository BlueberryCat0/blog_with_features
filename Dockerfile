FROM python:3.5
RUN apt-get update
RUN apt-get install -y gettext
RUN mkdir /code
WORKDIR /code
ADD req.txt /code/
RUN pip install -r req.txt
ADD . /code/
RUN python ./manage.py collectstatic --noinput

FROM python:3

MAINTAINER Greg Svoboda "grgesvo@gmail.com"

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.pip /app/requirements.pip

WORKDIR /app

RUN pip install -r requirements.pip

COPY . /app

WORKDIR /app/craigslist

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]

#docker run --name flask_cd --rm -p 5000:5000 --env MONGOPW --env DB_USER --env DB_PORT --env DB_PASSWORD --env DB_NAME --env SECRET_KEY flask
#sudo docker run --name flask_cd --rm -p 5000:5000 --env-file vertica.list flask &>/dev/null &
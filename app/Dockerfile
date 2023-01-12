# pull official base image
FROM python:3.8-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# more environment variables
RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential libpoppler-cpp-dev pkg-config gcc python3-dev \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies \
  && apt-get install -y  python3-pandas python-scipy \
  && apt-get install -y netcat \
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/* \
  && pip install djangorestframework markdown django-filter django-maintenance-mode requests Pillow # Filtering support


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

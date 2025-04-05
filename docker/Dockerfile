ARG PYTHON_VERSION=3.11.11-alpine

# pull official base image
FROM python:$PYTHON_VERSION AS builder

# set local variables
ARG APP_HOME=/code
ARG APP_DOCKER=/docker

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ENV TZ=America/Maceio
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# set work directory
WORKDIR $APP_HOME


# pull from builder image
FROM builder AS compiler

# copy dependencies
COPY ./requirements/production.txt $APP_HOME/requirements.txt

# install dependencies
RUN set -ex \
    && apk add --no-cache --virtual .build-deps \
        postgresql-dev \
        build-base \
        python3-dev \
        musl-dev \
        unixodbc-dev \
    && apk add --no-cache \
        build-base \
        cairo-dev \
        zlib-dev \
        libzip-dev \
        jpeg-dev \
        libpng-dev \
        libffi-dev \
        glib \
        pango \
        harfbuzz \
        fontconfig \
        freetype-dev \
    && python3 -m venv $VIRTUAL_ENV \
    && . $VIRTUAL_ENV/bin/activate \
    && pip install --no-cache-dir -U pip setuptools \
    && pip install --no-cache-dir -r $APP_HOME/requirements.txt \
    && pip cache purge \
    && deactivate \
    && apk del .build-deps \
    && rm -rf /tmp/*


# pull from builder image
FROM builder

# copy virtual environments
COPY --from=compiler /opt/venv /opt/venv

# copy project
COPY . .

# install dependencies
RUN set -ex \
    && apk add --no-cache \
        nginx \
        libpq \
        openrc \
        libmagic \
        glib \
        pango \
        libstdc++ \
        unixodbc-dev \
    && mkdir -p /var/log/supervisor \
    && mkdir -p /var/run/gunicorn \
    && rm -rf /tmp/*

# copy configs
COPY $APP_DOCKER/configs/nginx.conf /etc/nginx/http.d/default.conf

# copy scripts
COPY $APP_DOCKER/scripts/entrypoint.sh /entrypoint.sh
COPY $APP_DOCKER/scripts/app /start-app
COPY $APP_DOCKER/scripts/worker /start-worker

# set permission
RUN chmod +x /entrypoint.sh
RUN chmod +x /start-app
RUN chmod +x /start-worker

# run script
CMD ["/entrypoint.sh"]

ARG PYTHON_VERSION=3.10.11-alpine

# pull official base image
FROM python:$PYTHON_VERSION as compiler

# set local variables
ARG APP_HOME=/code
ARG APP_DOCKER=/docker

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# set work directory
WORKDIR $APP_HOME

# copy dependencies
COPY ./requirements/production.txt $APP_HOME/requirements.txt

# install dependencies
RUN set -ex \
    && apk add --no-cache --virtual .build-deps \
        postgresql-dev \
        build-base \
        python3-dev \
        musl-dev \
    && apk add --no-cache \
        build-base \
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
    && pip install -U pip setuptools \
    && pip install --no-cache-dir -r $APP_HOME/requirements.txt \
    && deactivate \
    && apk del .build-deps \
    && rm -rf /tmp/*

# pull official base image
FROM python:$PYTHON_VERSION

# copy virtual environments
COPY --from=compiler /opt/venv /opt/venv

# set local variables
ARG APP_HOME=/code
ARG APP_DOCKER=/docker

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# set work directory
WORKDIR $APP_HOME

# copy project
COPY . .

# install fonts
RUN set -ex \
	&& apk add --no-cache \
        ttf-freefont \
        font-noto \
        terminus-font \
    && fc-cache -f \
    && rm -rf /tmp/*

# install dependencies
RUN set -ex \
	&& apk add --no-cache \
        nginx \
        libpq \
        openrc \
        libmagic \
        glib \
        pango \
    && mkdir -p /var/run/gunicorn \
    && rm -rf /tmp/*

# copy configs
COPY $APP_DOCKER/configs/nginx.conf /etc/nginx/http.d/default.conf

# copy scripts
COPY $APP_DOCKER/scripts/entrypoint /entrypoint
COPY $APP_DOCKER/scripts/start /start

# set permission
RUN chmod +x /entrypoint
RUN chmod +x /start

# run script
CMD ["/entrypoint"]

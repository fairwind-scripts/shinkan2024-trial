# Customized from: https://github.com/orgs/python-poetry/discussions/1879#discussioncomment-216865

ARG PYTHON_VERSION=3.11.8

FROM python:${PYTHON_VERSION}-slim as python-base

# python
ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    # make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1 \
    \
    # paths
    # this is where our requirements + virtual environment will live
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"


# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"


# `builder-base` stage is used to build deps + create our virtual environment
FROM python-base as builder-base
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    # deps for installing poetry
    curl \
    # deps for building python deps
    build-essential \
    # psycopg2 dependencies
    libpq-dev

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | python3 -

# copy project requiremexnt files here to ensure they will be cached.
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry config virtualenvs.in-project false \
    && poetry install --with dev


# `development` image is used during development / testing
FROM python-base as development

ENV LC_ALL=en_US.UTF-8 \
    TZ=JST-9 \
    TERM=xtermdocker-attachingdocker-attaching

WORKDIR $PYSETUP_PATH

# copy in our built poetry + venv
COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

RUN apt update && apt install -y \
    # Required for migrations
    postgresql-client \
    # Locales
    locales \
    && locale-gen en_US.UTF-8

# quicker install as runtime deps are already installed
RUN poetry config virtualenvs.in-project false \
    && poetry install --with dev

# will become mountpoint of our code
ENV PYTHONPATH="$PYTHONPATH:/fairwind"
WORKDIR /fairwind


# `production` image used for runtime
FROM python-base as production

ENV TZ=JST-9 \
    TERM=xtermdocker-attachingdocker-attaching

COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

RUN apt update && apt install -y \
    git \
    # Required for migrations
    postgresql-client \
    # Locales
    locales \
    && locale-gen en_US.UTF-8

# will become mountpoint of our code
ENV PYTHONPATH="$PYTHONPATH:/fairwind"

COPY . /fairwind

WORKDIR /fairwind

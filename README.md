# Goslar Event Prototype

[![Build Status](https://travis-ci.com/DanielGrams/gsevpt.svg?branch=master)](https://travis-ci.com/DanielGrams/gsevpt) [![Coverage Status](https://coveralls.io/repos/github/DanielGrams/gsevpt/badge.svg?branch=master)](https://coveralls.io/github/DanielGrams/gsevpt?branch=master) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) ![Docker Pulls](https://img.shields.io/docker/pulls/danielgrams/gsevpt)

Website prototype using Python, Flask and Postgres.

## Automatic Deployment

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Docker

```sh
docker run -p 5000:5000 -e "DATABASE_URL=postgresql://postgres@localhost/gsevpt" danielgrams/gsevpt:latest
```

## Manual Installation

### Requirements

- Python 3.7
- pip
- Postgres with postgis

### Create database

```sh
psql -c 'create database gsevpt;' -U postgres
```

### Install and run

```sh
export DATABASE_URL="postgresql://postgres@localhost/gsevpt"
pip install -r requirements.txt
flask db upgrade
gunicorn --bind 0.0.0.0:5000 project:app
```

## Scheduled/Cron jobs

Jobs that should run on a regular basis.

### Daily

```sh
flask event update-recurring-dates
```

## Administration

```sh
flask user add-admin-roles super@hero.com
```

## Configuration

Create `.env` file in the root directory or pass as environment variables.

### Security

| Variable | Function |
| --- | --- |
| SECRET_KEY | A secret key for verifying the integrity of signed cookies. Generate a nice key using secrets.token_urlsafe(). |
| SECURITY_PASSWORD_HASH | Bcrypt is set as default SECURITY_PASSWORD_HASH, which requires a salt. Generate a good salt using: secrets.SystemRandom().getrandbits(128). |

### Send notifications via Mail

| Variable | Function |
| --- | --- |
| MAIL_DEFAULT_SENDER | see <https://pythonhosted.org/Flask-Mail/> |
| MAIL_PASSWORD | " |
| MAIL_PORT | " |
| MAIL_SERVER | " |
| MAIL_USERNAME | " |

### Resolve addresses with Google Maps

| Variable | Function |
| --- | --- |
| GOOGLE_MAPS_API_KEY | API Key with Places API enabled |

## Development

[Development](doc/development.md)

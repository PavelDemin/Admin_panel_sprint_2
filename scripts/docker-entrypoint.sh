#!/usr/bin/env bash

gunicorn --bind 'localhost:8000' config.wsgi:application

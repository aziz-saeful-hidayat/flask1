#!/bin/sh
alembic downgrade base
rm -rf migrations/versions/*
alembic revision --autogenerate -m "initial db"
alembic upgrade heads
python ./web_app/scripts/initializedb.py
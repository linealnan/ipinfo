#!/usr/bin/env bash
flask db history --directory ./migrations && flask db upgrade --directory ./migrations && flask fill_db && gunicorn --bind 0.0.0.0:5001 --timeout 600 -w 4 app:app && flask load_init_catalogs

#!/bin/bash

echo 'Export env vars for enablement of dev environment and start app'

export FLASK_APP=flask_hello_world.py
export FLASK_ENV=development

flask run

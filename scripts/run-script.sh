#!/usr/bin/env bash

set -euxo pipefail

touch ./backend/.env
touch ./frontend/.env
touch ./.env

docker compose down -v --remove-orphans

docker compose build
docker compose up -d

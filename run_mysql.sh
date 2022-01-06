#!/usr/bin/env bash

docker run --rm --name cleaning-gg-mysql-development \
  -e MYSQL_ROOT_PASSWORD=cleaning1234 \
  -e MYSQL_ROOT_HOST='%' \
  -e MYSQL_DATABASE=cleaning-gg \
  -p 3306:3306 mysql:8.0.23
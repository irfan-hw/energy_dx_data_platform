# energy_dx_data_platforms

## Docker Build
docker-compose up -d --build

## Import SQL Dump to Database
Import DB via localhost:3011

## Run program
docker-compose exec app bash
nohup python kishou_data_torikomi/src/main.py & python manage.py runserver 0.0.0.0:8011

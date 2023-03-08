# energy_dx_data_platforms

## Docker Build
docker-compose up -d --build

## Import SQL Dump to Database
Import DB via localhost:3011

## Run program
- Enter Container : docker-compose exec app bash
- Migrate Django : python manage.py migrate
- Create Django Admin : python manage.py createsuperuser
- Run Program on background: nohup python -u kishou_data_torikomi/src/main.py & python -u manage.py runserver 0.0.0.0:8011 &

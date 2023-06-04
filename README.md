# Django-REST
Pre-configured django 4.2.1 project with Vue JS 3. This configuration uses Webpack to supply static files to Django at development time Thus being able to use Django's SessionAuth avoiding Atuh via Token

## Prerequisites
required `python 3.11`

pip `23.0.1`

Docker

Node JS `18.16.0`

## Commands

### Virtual Enviroment 
Create virtual enviroment
``` bash
python -m vev venv
```
Activate virtual enviroment
``` bash
./venv/Scripts/activate # Windows only
source venv/bin/activate # MacOs
source bin/activate # Linux
```
Deactivate virtual enviroment
``` bash
deactivate
```
### Docker
Create database with docker 
``` bash
cd django
docker compose -f docker/docker-compose.yaml build
docker compose -f docker/docker-compose.yaml up -d
```
### Django
Start django apps
``` bash
cd django
python manage.py migrate # Only first run
python manage.py runserver
```
### Vue (Node JS)
``` bash
cd frontend
npm install # Only first run
npm run dev
```

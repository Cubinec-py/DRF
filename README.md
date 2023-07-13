# API: Service for searching nearest trucks for cargos delivery.

## Project information
- Creation of a new cargo (characteristics of pick-up, delivery locations are determined by the entered zip code);
- Getting a list of cargoes (pick-up, delivery locations, number of nearest trucks to the cargo ( =< 450 miles));
- Getting a list of cargoes with filters (weight, miles of nearest cars to cargo);
- Obtaining information about a specific cargo by ID (pick-up location, delivery, weight, description, list of numbers of ALL trucks with a distance to the selected cargo);
- Editing truck by ID (location (determined by the entered zip code));
- Editing cargo by ID (weight, description);
- Removing cargo by ID.
- Automatic update of the locations of all trucks every 3 minutes (the location changes to another random one).
- Project already have location data(30000 objects) and truck data when starting.

## Project environment
Create .env.dev in the root of the project and set the variables
```dotenv
PROJECT_SECRET_KEY=

POSTGRES_DB=
POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_USER=
POSTGRES_PASSWORD=


REDIS_HOST=
REDIS_PORT=
REDIS_URL=
REDIS_CACHE=

CELERY_BROKER_URL=
CELERY_RESULT_BACKEND=
```
Create .env.local in the root of the project and set the variables
```dotenv
PROJECT_SECRET_KEY=
```

## Project local settings
First, need to install the dependencies:
```bash
pip install -r requirements.txt
```
Before running the project, need to migrate the database:
```bash
python src/manage.py migrate --settings=core.settings.local
```
Now can run the project:
```bash
python src/manage.py runserver --settings=core.settings.local
```
To start celery worker:
```bash
cd src
celery -A core worker -l info
```

## Project dev settings
To start project just need to make one command
```bash
docker-compose up -d
```
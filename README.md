Running App using Docker:
> docker build -t mydigiez .
> docker run -d -p 5001:5001 mydigiez

Running App using virtual env:
> python -m venv env
> pip install -r requirements.txt
> python runserver.py


Migrations are like version control for your database, 
allowing your team to easily modify and share the application's database schema. .
Run migrations initialization, using the db init command as follows:
> python migrate.py db init

migration script will generate the tables that will persist.
Run the migration:
> python migrate.py db migrate
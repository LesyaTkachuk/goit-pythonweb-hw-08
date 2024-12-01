# goit-pythonweb-hw-08

REST API with CRUD operations support for efficient contact storage and management using the FastAPI framework, following a multilayer architecture for improved maintainability and scalability. The API leverages SQLAlchemy as the ORM to interact with a PostgreSQL database, enabling robust data storage and retrieval capabilities.

To run the poetry environment:

```
poetry shell
```

To install all dependencies:

```
poetry install
```

1. To run the database in the docker container using volumes for external data storage:

Create volume folder first:

```
docker volume create hw08-volume
```

Then run docker in container with volume attached:

```
docker run --name hw08-postgres -v hw08-volume:/var/lib/postgresql/data -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

2. Connect to the database through localhost:5432 using DBeaver for example and create database with the name "contacts_app" if it is not exist

Alternatevely you can create database directely in docker container following the next commands:

```
docker exec -it hw08-postgres psql -U postgres

create database contacts_app;

\l
\q
```

3. To run the initial migration:

```
alembic revision --autogenerate -m 'Init'
```

4. To apply initial migration to database and create tables from appointed models:

```
alembic upgrade head
```

5. To run app:

```
python main.py
```

6. For interaction with the server we can send requests using the Swagger on http://127.0.0.1:8000/docs
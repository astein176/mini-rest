# mini-rest
Small project utilizing Python with FastAPI, PostgreSQL, pytest, Docker, GitHub Actions

High level concepts explored REST, relational databases, containers, Dockers, and CI

To run: 
docker compose up --build

To test running service inside docker container: 
docker compose exec api pytest -v

To shutdown container: 
docker compose down 
  -- add -v to fully wipe container, allowing a full rebuild.


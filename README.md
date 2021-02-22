# Project was created to training my docker compose skills.

## About
This project consists of the Nginx provide a simple form, and make a request for app made in Python and this app send data for database and for Queue app to simulate e-mail sender aplication.

The imagem bellow represents project arquiteture:
</br>
<img src="https://i.ibb.co/wgSjbGf/Docker-architecture.png" width="490" height="400">

## How to run

```bash
# Check you have a Docker instaled and working properly.
# Open terminal and go to project directory
cd docker-email-workers

# Run Docker Compose in deamon mode flag (-d) and scale 3 workers containers
docker-compose up -d --scale worker=3

# Show docker worker log
docker-compose logs -f -t worker

# The server (ngix) starts at the door:80 - Go to http://localhost:80 
```

## Other commands

```bash
# Stops containers and removes containers, networks, volumes, and images created by up
docker-compose down

# Execute a sql command in db container
docker-compose exec db psql -U postgres -d email_sender -c 'select * from emails' 

# Show docker workers log
docker-compose logs -f -t worker
```

## Knowledges

- **[Docker Compose](https://docs.docker.com/compose/)**
- **[Docker Compose Override](https://docs.docker.com/compose/extends/)**
- **[Multi Instance](https://docs.docker.com/compose/reference/scale/)**

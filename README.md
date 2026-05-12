# Flask Redis Docker Compose App

## Beginner DevOps Portfolio Project

A multi-container application built with Flask, Redis, Docker Compose, and GitHub Actions.

---

## Features

- Flask web application
- Redis-backed page counter
- Docker containerization
- Multi-container setup with Docker Compose
- CI automation using GitHub Actions

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend language |
| Flask | Web framework |
| Redis | In-memory database |
| Docker | Containerization |
| Docker Compose | Multi-container orchestration |
| GitHub Actions | CI automation |

---

## Application Preview

### Homepage

![App Screenshot](images/app-screenshot.png)

---

## Project Structure

```text
flask-redis-compose-app/
├── .github/
│   └── workflows/
│       └── docker-compose.yml
├── Dockerfile
├── docker-compose.yml
├── app.py
├── requirements.txt
└── README.md
```

---

## Running the Application

### Start Containers

```bash
docker compose up --build
```

### Stop Containers

```bash
docker compose down
```

### Access the App

```text
http://localhost:5000
```

---

## GitHub Actions CI

This project automatically:

- Builds the Docker containers
- Starts the services
- Tests the Flask application
- Verifies the health endpoint

on every push to the `main` branch.

---

## What I Learned

- Docker image creation
- Docker Compose networking
- Container communication
- Redis integration
- CI/CD basics with GitHub Actions
- Health checks and service validation

---

## Future Improvements

- Add persistent Redis volumes
- Add Nginx reverse proxy
- Deploy to Azure
- Add monitoring with Prometheus/Grafana
- Add automated testing with pytest

---

## Author

**Matt Driscoll**

GitHub: https://github.com/mrdrisk


# FastAPI Project with PostgreSQL and LangChain

A modern FastAPI application with PostgreSQL database integration and LangChain capabilities.

## Features

- FastAPI backend with modern Python practices
- PostgreSQL database integration
- SQLAlchemy ORM for database operations
- Alembic for database migrations
- LangChain integration for AI capabilities
- Docker containerization
- Environment configuration with Pydantic
- Secure API key management

## Prerequisites

- Docker and Docker Compose installed on your system
- Git (for cloning the repository)

## Running with Docker

### 1. Clone the Repository
```bash
git clone <repository-url>
cd backendThesis
```

### 2. Create Environment File
Create a `.env` file in the project root with these variables:
```
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_db
POSTGRES_HOST=db
POSTGRES_PORT=5432
OPENAI_API_KEY=your_openai_api_key
```

### 3. Build and Start Containers
```bash
# Build the containers
docker-compose build

# Start all services in detached mode
docker-compose up -d

# To see logs while containers are running
docker-compose logs -f
```

### 4. Initialize the Database
```bash
# Run database migrations
docker-compose exec app alembic upgrade head
```

### 5. Access the Application
- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Common Docker Commands
```bash
# Stop all containers
docker-compose down

# Restart containers
docker-compose restart

# View container logs
docker-compose logs -f app  # For FastAPI app logs
docker-compose logs -f db   # For database logs

# Access container shell
docker-compose exec app bash

# Rebuild and restart
docker-compose up --build -d
```

### Troubleshooting
- If containers fail to start, check logs: `docker-compose logs`
- If database connection issues occur, ensure PostgreSQL container is running: `docker-compose ps`
- To reset everything: `docker-compose down -v` (this will remove volumes)

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── base.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── base.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       └── endpoints/
│   │           ├── __init__.py
│   │           └── base.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── db/
│   │   ├── __init__.py
│   │   └── session.py
│   └── services/
│       ├── __init__.py
│       └── base.py
├── migrations/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

## Dependencies

Key dependencies are managed in `pyproject.toml`:
- FastAPI
- Uvicorn
- SQLAlchemy
- PostgreSQL
- LangChain
- OpenAI
- Pydantic
- Alembic

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
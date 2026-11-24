# Clinova

**Online Clinic Appointment Booking System**

Clinova is a RESTful backend application for managing doctors and booking medical appointments in a single clinic. It is built with FastAPI and follows a Modular Monolith architecture.

## Tech Stack

- **Python 3.12+**
- **FastAPI** – Web framework
- **PostgreSQL** – Relational database
- **SQLAlchemy 2.0** – ORM
- **Alembic** – Database migrations
- **Pydantic v2** – Data validation and settings
- **Uvicorn** – ASGI server
- **Elasticsearch** – Doctor search (planned)

## Architecture

Clinova follows the **Modular Monolith** architecture, organizing the application into independent modules while keeping everything in a single deployable application.

```text
app/
├── api/
│   └── v1/
├── core/
├── database/
├── integrations/
└── modules/
    ├── auth/
    ├── doctors/
    ├── appointments/
    └── health/
```

## Current Features

- Modular Monolith architecture
- RESTful API structure
- API versioning
- PostgreSQL integration
- Asynchronous database connection with SQLAlchemy
- Database migration management with Alembic
- Centralized application settings
- Custom exception handling
- Health check endpoints

## Planned Features

- User authentication and authorization
- Doctor and patient management
- Appointment booking and management
- Appointment availability and scheduling
- Online payment integration
- Real-time appointment updates using WebSockets
- Doctor search using Elasticsearch

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Ali-Ghoreishi/clinova.git
cd clinova
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```powershell
.\venv\Scripts\Activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
APP_NAME=Clinova
DEBUG=True
APP_PORT=7070

DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/clinova_db
```

Update the database credentials according to your PostgreSQL configuration.

### 5. Run the application

```bash
python run.py
```

The application will be available at:

```text
http://127.0.0.1:7070
```

## API Documentation

FastAPI automatically generates interactive API documentation.

- **Swagger UI:** http://127.0.0.1:7070/docs
- **ReDoc:** http://127.0.0.1:7070/redoc

## Database Migrations

Create a new migration:

```bash
alembic revision --autogenerate -m "migration message"
```

Apply migrations:

```bash
alembic upgrade head
```

Check the current migration:

```bash
alembic current
```

## License

This project is currently developed as a personal portfolio project.
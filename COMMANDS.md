# Clinova – Commands

## 1. Ruff (Code Formatting & Linting)

Format all Python files:

```bash
python -m ruff format .
```

Check and fix linting issues:

```bash
python -m ruff check . --fix
```

Organize imports:

```bash
python -m ruff check . --select I --fix
```

## 2. Virtual Environment

Create virtual environment:

```bash
python -m venv venv
```

Activate on Windows (PowerShell):

```powershell
.\venv\Scripts\Activate
```

Deactivate:

```bash
deactivate
```

## 3. Install Dependencies

```bash
pip install fastapi "uvicorn[standard]" pydantic-settings sqlalchemy asyncpg
```

Save dependencies:

```bash
pip freeze > requirements.txt
```

Install dependencies from file:

```bash
pip install -r requirements.txt
```

## 4. Run Application

```bash
python run.py
```

Application:

```text
http://127.0.0.1:7070
```

Swagger UI:

```text
http://127.0.0.1:7070/docs
```

ReDoc:

```text
http://127.0.0.1:7070/redoc
```

## 5. PostgreSQL

Database:

```text
clinova_db
```

Connection string is configured in `.env` using `DATABASE_URL`.

## 6. Git

(To be added)

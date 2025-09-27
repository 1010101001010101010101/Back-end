# EcoEnergy (U2 - Avance BD + Seeds + Admin)
## Requisitos
- Python 3.13
- pip, venv

## Instalación
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt (opcional)

## Configuración
Copiar .env.example a .env (usamos SQLite)
DJANGO_DEBUG=True

## Migraciones y seeds
python manage.py makemigrations
python manage.py migrate
python manage.py seed_catalog
python manage.py seed_demo_data

## Correr
python manage.py runserver

## Acceso admin
Usuario: keyla (o el que hayas creado)

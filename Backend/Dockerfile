# Usar la versión de Python 3.11.9
FROM python:3.11.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requerimientos
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Exponer el puerto de FastAPI
EXPOSE 8000

# Comando para correr el servidor de FastAPI y Celery
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 & celery -A celery_worker worker --loglevel=info"]

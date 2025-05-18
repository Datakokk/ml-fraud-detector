# Usa una imagen base mínima oficial de Python
FROM python:3.10-slim

# Evita prompts de apt
ENV DEBIAN_FRONTEND=noninteractive

# Establece el directorio de trabajo
WORKDIR /app

# Instala dependencias del sistema necesarias para algunas bibliotecas Python (si las necesitas)
# Puedes quitar esto si tu proyecto no usa pandas, numpy, etc.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copia los archivos del proyecto
COPY ./app .
COPY requirements.txt .

# Instala dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p app/model && python app/utils/train_model.py

# Expón el puerto (opcional pero recomendable)
EXPOSE 8080

# Usa el comando recomendado para Uvicorn en FastAPI
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080}"]

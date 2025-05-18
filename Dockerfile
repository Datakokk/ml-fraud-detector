# Usa una imagen base mínima oficial de Python
FROM python:3.10-slim

# Evita prompts de apt
ENV DEBIAN_FRONTEND=noninteractive

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Añade el path /app al PYTHONPATH para que se pueda importar el paquete "app"
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Instala dependencias del sistema necesarias para algunas bibliotecas Python
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copia todos los archivos del proyecto
COPY . .

# Instala dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Entrena y guarda el modelo
RUN python app/utils/train_model.py

# Expón el puerto
EXPOSE 8080

# Ejecuta la aplicación con uvicorn apuntando a app.main:app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

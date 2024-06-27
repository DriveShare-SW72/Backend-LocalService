# Usar una imagen base de Python
FROM python:3.9

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instalar las dependencias directamente en el entorno base de Python
RUN pip install -r requirements.txt

# Copiar el resto del código al contenedor
COPY . .

# Ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
